"""Servis katmanı: generate_bridge ve evaluate_attempt (v2 §5)."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional, Protocol

from pydantic import ValidationError

from . import prompts
from .contracts import (
    MAX_PHRASE_CHARS,
    MAX_RATIONALE_CHARS,
    MAX_SOURCE_CHARS,
    OPTION_IDS,
    AttemptFeedback,
    BridgeError,
    BridgeRequest,
    BridgeResult,
    FeedbackDraft,
)
from .source import PhraseMatch, Segment, UnclosedCodeFence, find_phrase, split_source

FIXTURE_DIR = Path(__file__).resolve().parent.parent / "fixtures"
DEV_LABEL = "GELİŞTİRME VERİSİ — canlı AI sonucu değildir"


class JsonModelClient(Protocol):
    def generate_json(self, system: str, user: str, schema: Optional[dict[str, Any]]) -> dict[str, Any]: ...


def prompt_version() -> str:
    v = os.getenv("PROMPT_VERSION", "few_shot").strip()
    return v if v in prompts.PROMPT_VERSIONS else "few_shot"


# ---------------------------------------------------------------- girdi kontrolü (API öncesi)
def check_request(source_text: str, selected_phrase: str, subject_label: Optional[str] = None
                  ) -> tuple[BridgeRequest, list[Segment], PhraseMatch]:
    if not source_text or not source_text.strip():
        raise BridgeError("invalid_input", "Kaynak metin boş. Bir demo metni seçin ya da kendi metninizi yapıştırın.")
    if len(source_text) > MAX_SOURCE_CHARS:
        raise BridgeError("invalid_input", f"Kaynak metin en fazla {MAX_SOURCE_CHARS:,} karakter olabilir "
                                           f"(şu an {len(source_text):,}).".replace(",", "."))
    if not selected_phrase or not selected_phrase.strip():
        raise BridgeError("invalid_input", "Zorlandığınız ifadeyi kaynak metinden kopyalayıp ilgili alana yapıştırın.")
    if len(selected_phrase) > MAX_PHRASE_CHARS:
        raise BridgeError("invalid_input", f"Seçilen ifade en fazla {MAX_PHRASE_CHARS} karakter olabilir. "
                                           "Yalnızca zorlandığınız kısmı seçin.")
    try:
        segments = split_source(source_text)
    except UnclosedCodeFence:
        raise BridgeError("invalid_input", "Kaynakta ``` ile açılmış bir kod bloğu kapatılmamış. "
                                           "Kod bloğunun sonuna ayrı satırda ``` ekleyin.") from None
    if not segments:
        raise BridgeError("invalid_input", "Kaynak metinde işlenecek içerik bulunamadı.")
    match = find_phrase(segments, selected_phrase)
    if match.status == "not_found":
        raise BridgeError("invalid_input", "Seçilen ifade kaynak metinde bulunamadı. İfadeyi kaynaktan doğrudan "
                                           "kopyalayın; tırnak işaretleri ve harfler aynı olmalı.")
    if match.status == "ambiguous":
        raise BridgeError("invalid_input", f"Seçilen ifade kaynakta {match.count} yerde geçiyor. "
                                           "İfadeyi çevresindeki birkaç kelimeyle genişletin.")
    req = BridgeRequest(source_text=source_text, selected_phrase=selected_phrase,
                        subject_label=(subject_label or None))
    return req, segments, match


def check_attempt(bridge: BridgeResult, selected_option_id: Optional[str], rationale: Optional[str]) -> str:
    if bridge.status != "ready" or bridge.quiz is None:
        raise BridgeError("invalid_input", "Bu sonuç için cevaplanacak soru yok.")
    if selected_option_id not in OPTION_IDS:
        raise BridgeError("invalid_input", "Lütfen bir seçenek işaretleyin.")
    r = (rationale or "").strip()
    if not r:
        raise BridgeError("invalid_input", "Lütfen seçiminizin kısa gerekçesini yazın.")
    if len(r) > MAX_RATIONALE_CHARS:
        raise BridgeError("invalid_input", f"Gerekçe en fazla {MAX_RATIONALE_CHARS} karakter olabilir.")
    return r


# ---------------------------------------------------------------- doğrulama
def _validate_bridge(raw: dict[str, Any], segments: list[Segment]) -> BridgeResult:
    result = BridgeResult.model_validate(raw)
    valid_ids = {s.id for s in segments}
    bad = [r for r in result.source_refs if r not in valid_ids]
    if bad:
        raise ValueError(f"Geçersiz kaynak referansı: {bad}")
    if result.status == "ready" and not result.source_refs:
        raise ValueError("ready sonucunda en az bir kaynak referansı gerekir.")
    result.source_refs = list(dict.fromkeys(result.source_refs))  # tekrarları at, sırayı koru
    return result


# ---------------------------------------------------------------- ana servisler
def generate_bridge(request: BridgeRequest, client: Optional[JsonModelClient] = None, *,
                    dev_fixture: Optional[str] = None) -> BridgeResult:
    """Açıklama + terimler + örnek + soru üretir.

    dev_fixture verilirse ("ready" / "insufficient_source") model çağrılmaz ve etiketli
    geliştirme verisi döner.
    """
    _, segments, match = check_request(request.source_text, request.selected_phrase, request.subject_label)

    if dev_fixture:
        return load_fixture_result(dev_fixture)

    if client is None:
        from .gemini_client import GeminiClient
        client = GeminiClient()

    system = prompts.bridge_system_prompt(prompt_version())
    user = prompts.bridge_user_payload(segments, request.selected_phrase, request.subject_label, match.segment_ids)

    last_err = ""
    for attempt in range(2):  # biçim hatasında bir kez yeniden dene
        raw = client.generate_json(system, user, prompts.BRIDGE_SCHEMA)
        try:
            return _validate_bridge(raw, segments)
        except (ValidationError, ValueError) as e:
            last_err = str(e)[:300]
    raise BridgeError("invalid_output", detail=last_err)


def evaluate_attempt(request: BridgeRequest, bridge: BridgeResult, selected_option_id: str,
                     rationale: str, client: Optional[JsonModelClient] = None, *,
                     dev: bool = False) -> AttemptFeedback:
    r = check_attempt(bridge, selected_option_id, rationale)
    assert bridge.quiz is not None
    # Doğruluk kararı yalnızca burada, kodla verilir. Model metni bunu değiştiremez.
    is_correct = selected_option_id == bridge.quiz.correct_option_id

    if dev:
        draft = load_fixture_feedback(is_correct)
    else:
        if client is None:
            from .gemini_client import GeminiClient
            client = GeminiClient()
        user = prompts.feedback_user_payload(
            request.selected_phrase, bridge.simple_explanation, bridge.quiz.model_dump(),
            selected_option_id, is_correct, r, source_text=request.source_text,
        )
        draft = None
        last_err = ""
        for _ in range(2):
            raw = client.generate_json(prompts.FEEDBACK_RULES, user, prompts.FEEDBACK_SCHEMA)
            try:
                draft = FeedbackDraft.model_validate(raw)
                break
            except ValidationError as e:
                last_err = str(e)[:300]
        if draft is None:
            raise BridgeError("invalid_output", detail=last_err)

    return AttemptFeedback(is_correct=is_correct, strengths=draft.strengths,
                           improvements=draft.improvements, retry_hint=draft.retry_hint)


# ---------------------------------------------------------------- geliştirme verisi
def _read_fixture(name: str) -> dict[str, Any]:
    with open(FIXTURE_DIR / name, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("_note", None)
    return data


def load_fixture_result(kind: str) -> BridgeResult:
    name = {"ready": "bridge_ready.json", "insufficient_source": "bridge_insufficient_source.json"}[kind]
    return BridgeResult.model_validate(_read_fixture(name))


def load_fixture_feedback(is_correct: bool) -> FeedbackDraft:
    data = _read_fixture("feedback_examples.json")
    return FeedbackDraft.model_validate(data["correct" if is_correct else "incorrect"])
