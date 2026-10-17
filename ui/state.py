"""Oturum durumu (v2 §6.2). Streamlit'ten bağımsızdır; sözlük benzeri her yapıyla test edilebilir.

- Girdi kimliği (parmak izi) ORİJİNAL kaynak + ifade + ders etiketinden üretilir.
- Girdi değişince açıklama, soru, seçili şık, gerekçe ve geri bildirim temizlenir.
- Cevap formu anahtarları `answer_nonce` içerir; nonce artınca radio/gerekçe sıfırlanır.
- Parmak izi API çağrısı TETİKLEMEZ; çağrılar yalnızca düğme/form gönderimindedir.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, MutableMapping, Optional

WORK = "work"
FEEDBACK = "feedback"
NONCE = "answer_nonce"


def fingerprint(source_text: str, selected_phrase: str, subject_label: Optional[str]) -> str:
    payload = json.dumps([subject_label or "", source_text, selected_phrase], ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _bump(state: MutableMapping[str, Any]) -> None:
    state[NONCE] = int(state.get(NONCE, 0)) + 1


def clear_work(state: MutableMapping[str, Any]) -> None:
    state.pop(WORK, None)
    state.pop(FEEDBACK, None)
    _bump(state)


def sync_work(state: MutableMapping[str, Any], fp: str) -> bool:
    """Girdi değiştiyse eski çalışmayı temizler. Temizlediyse True döner."""
    work = state.get(WORK)
    if work is not None and work.get("fp") != fp:
        clear_work(state)
        return True
    return False


def store_bridge(state: MutableMapping[str, Any], fp: str, request: Any, bridge: Any, is_dev: bool) -> None:
    state[WORK] = {"fp": fp, "request": request, "bridge": bridge, "is_dev": is_dev}
    state.pop(FEEDBACK, None)
    _bump(state)


def store_feedback(state: MutableMapping[str, Any], fp: str, feedback: Any, choice: str) -> bool:
    work = state.get(WORK)
    if work is None or work.get("fp") != fp:
        return False  # girdi değişmişse eski geri bildirim yeni girdiye yazılmaz
    state[FEEDBACK] = {"fp": fp, "feedback": feedback, "choice": choice}
    return True


def reset_answer(state: MutableMapping[str, Any]) -> None:
    state.pop(FEEDBACK, None)
    _bump(state)


def current_work(state: MutableMapping[str, Any], fp: str) -> Optional[dict[str, Any]]:
    work = state.get(WORK)
    return work if work is not None and work.get("fp") == fp else None


def current_feedback(state: MutableMapping[str, Any], fp: str) -> Optional[dict[str, Any]]:
    fb = state.get(FEEDBACK)
    return fb if fb is not None and fb.get("fp") == fp else None
