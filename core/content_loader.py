"""content/*.json ders dosyalarını yükler (içerik: Mehmet Ali, yükleyici: İrem)."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from pydantic import ValidationError

from .contracts import LessonContent

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
DEV_INPUT = ROOT / "fixtures" / "dev_input_python.json"


@dataclass
class LoadReport:
    lessons: list[LessonContent]
    errors: list[str]  # dosya adı + kısa neden; UI'da geliştirici uyarısı olarak gösterilir
    using_dev_input: bool


def _load_file(path: Path) -> LessonContent:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("_note", None)
    return LessonContent.model_validate(data)


def load_lessons(content_dir: Path = CONTENT_DIR) -> LoadReport:
    lessons: list[LessonContent] = []
    errors: list[str] = []
    if content_dir.is_dir():
        for path in sorted(content_dir.glob("*.json")):
            try:
                lessons.append(_load_file(path))
            except (OSError, json.JSONDecodeError, ValidationError) as e:
                first = str(e).splitlines()[0][:160]
                errors.append(f"{path.name}: {first}")
    ids = [l.id for l in lessons]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errors.append(f"Tekrarlanan ders kimliği: {sorted(dup)}")
    if lessons:
        return LoadReport(lessons, errors, using_dev_input=False)
    return LoadReport([_load_file(DEV_INPUT)], errors, using_dev_input=True)
