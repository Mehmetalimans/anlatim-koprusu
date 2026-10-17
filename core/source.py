"""Kaynak bölme (P1, P2…) ve seçilen ifadenin kaynakta bulunması.

Kurallar (v2 §6.1, §6.3):
- Orijinal kaynak değiştirilmez; eşleşme için ayrı karşılaştırma kopyası üretilir.
- Düzyazı: Unicode NFC + boşluk sadeleştirme. Büyük/küçük harf dönüşümü YOK.
- Kod blokları: yalnızca satır sonu farkları eşitlenir; girinti/satırlar korunur.
- Tırnaklar otomatik değiştirilmez.
- Üç ters tırnaklı kod blokları tek parça; içlerindeki boş satır paragraf sınırı değildir.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Literal

FENCE = "```"
_WS = re.compile(r"\s+")


@dataclass(frozen=True)
class Segment:
    id: str
    kind: Literal["prose", "code"]
    text: str
    lang: str = ""


class UnclosedCodeFence(ValueError):
    pass


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _is_fence(line: str) -> bool:
    return line.lstrip().startswith(FENCE)


def split_source(text: str) -> list[Segment]:
    """Kaynağı sıralı parçalara böler. Kapanmamış kod bloğunda UnclosedCodeFence."""
    lines = normalize_newlines(text).split("\n")
    raw: list[tuple[str, str, str]] = []  # (kind, text, lang)
    prose_buf: list[str] = []
    i = 0

    def flush_prose() -> None:
        if prose_buf:
            chunk = "\n".join(prose_buf).strip("\n")
            if chunk.strip():
                raw.append(("prose", chunk, ""))
            prose_buf.clear()

    while i < len(lines):
        line = lines[i]
        if _is_fence(line):
            flush_prose()
            lang = line.lstrip()[len(FENCE):].strip()
            code_lines: list[str] = []
            i += 1
            closed = False
            while i < len(lines):
                if lines[i].strip() == FENCE:
                    closed = True
                    break
                code_lines.append(lines[i])
                i += 1
            if not closed:
                raise UnclosedCodeFence("Kod bloğu ``` ile açılmış ama kapatılmamış.")
            raw.append(("code", "\n".join(code_lines), lang))
            i += 1
            continue
        if line.strip() == "":
            flush_prose()
        else:
            prose_buf.append(line)
        i += 1
    flush_prose()

    return [Segment(id=f"P{n}", kind=k, text=t, lang=lg) for n, (k, t, lg) in enumerate(raw, start=1)]


def _norm_prose(s: str) -> str:
    return _WS.sub(" ", unicodedata.normalize("NFC", s)).strip()


def _norm_code(s: str) -> str:
    return normalize_newlines(s)


def _count(hay: str, needle: str) -> int:
    if not needle:
        return 0
    n, start = 0, 0
    while True:
        idx = hay.find(needle, start)
        if idx < 0:
            return n
        n += 1
        start = idx + 1  # çakışan eşleşmeleri de say: belirsizlik gözden kaçmasın


@dataclass(frozen=True)
class PhraseMatch:
    count: int
    segment_ids: tuple[str, ...]

    @property
    def status(self) -> Literal["ok", "not_found", "ambiguous"]:
        if self.count == 0:
            return "not_found"
        return "ok" if self.count == 1 else "ambiguous"


def find_phrase(segments: list[Segment], phrase: str) -> PhraseMatch:
    """Seçilen ifadenin kaynakta kaç kez geçtiğini bulur (ilk yeri otomatik seçmez)."""
    prose_phrase = _norm_prose(phrase)
    code_phrase = _norm_code(phrase).strip("\n")
    total, ids = 0, []
    for seg in segments:
        if seg.kind == "prose":
            c = _count(_norm_prose(seg.text), prose_phrase)
        else:
            c = _count(_norm_code(seg.text), code_phrase)
        if c:
            total += c
            ids.append(seg.id)
    return PhraseMatch(count=total, segment_ids=tuple(ids))
