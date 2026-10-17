"""Ortak teknik sözleşme (v2, 17 Ekim 2026).

İçerik şemasını (LessonContent) veya BridgeResult/AttemptFeedback alanlarını
değiştiren her düzenleme Mehmet Ali'ye geçiş örneğiyle bildirilir.
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

MAX_SOURCE_CHARS = 6000
MAX_PHRASE_CHARS = 500
MAX_RATIONALE_CHARS = 1000
OPTION_IDS: tuple[str, ...] = ("A", "B", "C", "D")

OptionId = Literal["A", "B", "C", "D"]
Status = Literal["ready", "insufficient_source"]
ErrorCode = Literal["invalid_input", "missing_key", "quota", "network", "invalid_output"]


class _Strict(BaseModel):
    # Modelden gelen fazladan alanlar (ör. modelin uydurduğu is_correct) yok sayılır.
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)


# ---------------------------------------------------------------- istek
class BridgeRequest(_Strict):
    source_text: str = Field(min_length=1, max_length=MAX_SOURCE_CHARS)
    selected_phrase: str = Field(min_length=1, max_length=MAX_PHRASE_CHARS)
    subject_label: Optional[str] = Field(default=None, max_length=80)

    # Kaynak metindeki girinti ve boşluklar korunmalı: strip uygulanmaz.
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=False)


# ---------------------------------------------------------------- sonuç
class Term(_Strict):
    term: str = Field(min_length=1)
    explanation: str = Field(min_length=1)
    origin: Literal["source", "supporting"]


class Example(_Strict):
    text: str = Field(min_length=1)
    origin: Literal["generated"] = "generated"


class QuizOption(_Strict):
    id: OptionId
    text: str = Field(min_length=1)


class Quiz(_Strict):
    question: str = Field(min_length=1)
    options: list[QuizOption] = Field(min_length=4, max_length=4)
    correct_option_id: OptionId
    answer_explanation: str = Field(min_length=1)

    @model_validator(mode="after")
    def _check_options(self) -> "Quiz":
        ids = [o.id for o in self.options]
        if sorted(ids) != list(OPTION_IDS):
            raise ValueError("Seçenek kimlikleri tam olarak A, B, C, D olmalı ve tekrar etmemeli.")
        texts = [o.text.casefold() for o in self.options]
        if len(set(texts)) != 4:
            raise ValueError("Seçenek metinleri birbirinden farklı olmalı.")
        if self.correct_option_id not in ids:
            raise ValueError("Doğru seçenek kimliği seçenekler arasında yok.")
        self.options = sorted(self.options, key=lambda o: o.id)
        return self


class BridgeResult(_Strict):
    status: Status
    simple_explanation: str = Field(min_length=1)
    source_refs: list[str] = Field(default_factory=list)
    terms: list[Term] = Field(default_factory=list)
    example: Optional[Example] = None
    quiz: Optional[Quiz] = None
    warnings: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _check_status(self) -> "BridgeResult":
        if self.status == "ready":
            if self.quiz is None or self.example is None:
                raise ValueError("ready sonucunda quiz ve example zorunludur.")
        else:  # insufficient_source
            if self.quiz is not None:
                raise ValueError("insufficient_source sonucunda quiz null olmalıdır.")
        return self


class FeedbackDraft(_Strict):
    """Modelden beklenen geri bildirim metni. Doğruluk kararı burada YOK."""

    strengths: list[str] = Field(default_factory=list)
    improvements: list[str] = Field(default_factory=list)
    retry_hint: str = ""


class AttemptFeedback(_Strict):
    is_correct: bool  # Yalnızca uygulama kodu belirler (services.evaluate_attempt).
    strengths: list[str] = Field(default_factory=list)
    improvements: list[str] = Field(default_factory=list)
    retry_hint: str = ""


# ---------------------------------------------------------------- içerik şeması (content/*.json)
class LessonSource(_Strict):
    title: str = Field(min_length=1)
    url: str = Field(min_length=1)


class LessonContent(_Strict):
    """Mehmet Ali'nin content/ klasörüne yazacağı ders dosyalarının şeması.

    Öğrenci ekranında yalnızca id, subject_label, title, source_text,
    selected_phrase ve sources gösterilir. expected_meaning, invariants,
    correct_rationale, incorrect_rationale yalnızca kabul testleri içindir.
    """

    id: str = Field(min_length=1, pattern=r"^[a-z0-9_\-]+$")
    subject_label: str = Field(min_length=1, max_length=80)
    title: str = Field(min_length=1)
    source_text: str = Field(min_length=1, max_length=MAX_SOURCE_CHARS)
    selected_phrase: str = Field(min_length=1, max_length=MAX_PHRASE_CHARS)
    sources: list[LessonSource] = Field(default_factory=list)
    expected_meaning: str = ""
    invariants: list[str] = Field(default_factory=list)
    correct_rationale: str = ""
    incorrect_rationale: str = ""

    model_config = ConfigDict(extra="ignore", str_strip_whitespace=False)


# ---------------------------------------------------------------- hata
USER_MESSAGES: dict[str, str] = {
    "invalid_input": "Girdi kontrolden geçmedi.",
    "missing_key": "Yapay zekâ hizmetine erişilemedi: API anahtarı eksik, geçersiz ya da bu modele yetkisi yok.",
    "quota": "Ücretsiz kullanım sınırına ulaşıldı. Bir dakika bekleyip tekrar deneyin; günlük sınır dolduysa ertesi gün yenilenir.",
    "network": "Yapay zekâ hizmetine bağlanılamadı. İnternet bağlantısını kontrol edip tekrar deneyin.",
    "invalid_output": "Yapay zekâdan beklenen biçimde bir yanıt alınamadı. Lütfen tekrar deneyin.",
}


class BridgeError(Exception):
    """Kullanıcıya Türkçe gösterilebilen, anahtar/ham hata içermeyen hata."""

    def __init__(self, code: ErrorCode, user_message: Optional[str] = None, detail: str = ""):
        self.code = code
        self.user_message = user_message or USER_MESSAGES[code]
        self.detail = detail  # Yalnızca geliştirici günlüğü için; UI'da gösterilmez.
        super().__init__(f"{code}: {self.user_message}")
