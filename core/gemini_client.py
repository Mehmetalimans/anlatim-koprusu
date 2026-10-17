"""Gemini REST istemcisi (yalnızca standart kütüphane).

SDK yerine doğrudan `v1beta/models/{model}:generateContent` uç noktası kullanılır;
böylece bağımlılık azalır ve SDK sürüm farkları akışı bozmaz.
Anahtar URL'ye değil `x-goog-api-key` başlığına konur; hiçbir hata mesajına yazılmaz.
"""
from __future__ import annotations

import json
import os
import socket
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Optional

from .contracts import BridgeError

API_ROOT = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-3.5-flash-lite"


@dataclass
class CallMeta:
    model: str
    seconds: float
    used_schema: bool
    attempts: list[str] = field(default_factory=list)


def map_http_error(status: int, body: str) -> BridgeError:
    """HTTP hatasını sözleşmedeki hata kodlarına çevirir (ham gövde yalnızca detail'de)."""
    low = body.lower()
    short = f"HTTP {status}"
    if status == 429 or "resource_exhausted" in low or "quota" in low:
        return BridgeError("quota", detail=short)
    if status in (401, 403) or "api key" in low or "api_key" in low:
        return BridgeError("missing_key", detail=short)
    if status == 404:
        return BridgeError(
            "missing_key",
            "Model bulunamadı ya da bu anahtarla erişilemiyor. GEMINI_MODEL değerini kontrol edin.",
            detail=short,
        )
    if status >= 500:
        return BridgeError("network", "Yapay zekâ hizmeti şu anda yanıt vermiyor. Biraz sonra tekrar deneyin.", detail=short)
    return BridgeError("invalid_output", detail=short)


class GeminiClient:
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None,
                 timeout: float = 60.0, temperature: float = 0.4):
        self.api_key = (api_key if api_key is not None else os.getenv("GEMINI_API_KEY", "")).strip()
        self.model = (model or os.getenv("GEMINI_MODEL") or DEFAULT_MODEL).strip()
        self.timeout = timeout
        self.temperature = temperature
        self.last_meta: Optional[CallMeta] = None

    # ------------------------------------------------------------ düşük seviye
    def _post(self, url: str, body: dict[str, Any]) -> dict[str, Any]:
        req = urllib.request.Request(
            url,
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json", "x-goog-api-key": self.api_key},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                err_body = e.read().decode("utf-8", "replace")
            except Exception:
                err_body = ""
            raise map_http_error(e.code, err_body) from None
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as e:
            raise BridgeError("network", detail=type(e).__name__) from None
        except json.JSONDecodeError:
            raise BridgeError("invalid_output", detail="yanıt JSON değil") from None

    def _get(self, url: str) -> dict[str, Any]:
        req = urllib.request.Request(url, headers={"x-goog-api-key": self.api_key}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise map_http_error(e.code, e.read().decode("utf-8", "replace")) from None
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError) as e:
            raise BridgeError("network", detail=type(e).__name__) from None

    @staticmethod
    def _extract_text(data: dict[str, Any]) -> str:
        cands = data.get("candidates") or []
        if not cands:
            reason = (data.get("promptFeedback") or {}).get("blockReason", "aday yok")
            raise BridgeError("invalid_output", detail=f"boş yanıt: {reason}")
        parts = (cands[0].get("content") or {}).get("parts") or []
        text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
        if not text.strip():
            raise BridgeError("invalid_output", detail=f"metin yok: {cands[0].get('finishReason')}")
        return text

    # ------------------------------------------------------------ genel arayüz
    def list_models(self) -> list[str]:
        self._require_key()
        data = self._get(f"{API_ROOT}/models?pageSize=200")
        return [m.get("name", "").removeprefix("models/") for m in data.get("models", [])]

    def generate_json(self, system: str, user: str, schema: Optional[dict[str, Any]]) -> dict[str, Any]:
        """JSON çıktı üretir. Şema reddedilirse (HTTP 400) bir kez şemasız JSON kipiyle dener."""
        self._require_key()
        url = f"{API_ROOT}/models/{self.model}:generateContent"
        t0 = time.perf_counter()
        attempts: list[str] = []

        def body(with_schema: bool) -> dict[str, Any]:
            cfg: dict[str, Any] = {"responseMimeType": "application/json", "temperature": self.temperature}
            if with_schema and schema:
                cfg["responseSchema"] = schema
            return {
                "systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "user", "parts": [{"text": user}]}],
                "generationConfig": cfg,
            }

        used_schema = schema is not None
        try:
            data = self._post(url, body(True))
            attempts.append("schema" if used_schema else "json")
        except BridgeError as e:
            if not (used_schema and e.code == "invalid_output" and e.detail == "HTTP 400"):
                raise
            attempts.append("schema→400")
            data = self._post(url, body(False))
            attempts.append("json")
            used_schema = False

        text = self._extract_text(data)
        self.last_meta = CallMeta(self.model, round(time.perf_counter() - t0, 2), used_schema, attempts)
        try:
            return json.loads(_strip_code_fence(text))
        except json.JSONDecodeError:
            raise BridgeError("invalid_output", detail="model JSON üretmedi") from None

    def _require_key(self) -> None:
        if not self.api_key:
            raise BridgeError(
                "missing_key",
                "GEMINI_API_KEY bulunamadı. .env dosyasına anahtarı ekleyip uygulamayı yeniden başlatın.",
            )


def _strip_code_fence(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else ""
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    return t.strip()
