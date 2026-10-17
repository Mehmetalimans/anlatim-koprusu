"""IR-02: Gemini erişim ve uçtan uca akış denemesi (İrem'in bilgisayarında çalıştırılır).

Çalıştırma (proje kök klasöründe):
    python scripts/check_gemini.py

Yaptıkları:
1. GEMINI_API_KEY var mı (değerini yazdırmaz) ve GEMINI_MODEL hesapta listeleniyor mu?
2. Geliştirme girdisiyle (veya --content <dosya>) gerçek generate_bridge çağrısı.
3. Bir doğru, bir yanlış seçenekle gerçek evaluate_attempt çağrısı.
4. Sonucu tech_logs/api_check_<zaman>.json dosyasına yazar (anahtar YAZILMAZ).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
except ImportError:
    pass

from core.contracts import BridgeError, LessonContent  # noqa: E402
from core.gemini_client import GeminiClient  # noqa: E402
from core.services import check_request, evaluate_attempt, generate_bridge, prompt_version  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default=str(ROOT / "fixtures" / "dev_input_python.json"))
    args = ap.parse_args()

    client = GeminiClient()
    log: dict = {"time": datetime.now().isoformat(timespec="seconds"), "model": client.model,
                 "prompt_version": prompt_version(), "key_present": bool(client.api_key), "steps": []}

    def step(name: str, ok: bool, **info) -> None:
        log["steps"].append({"step": name, "ok": ok, **info})
        print(f"[{'OK ' if ok else 'HATA'}] {name} {json.dumps(info, ensure_ascii=False)[:600]}")

    if not client.api_key:
        step("anahtar", False, mesaj="GEMINI_API_KEY bulunamadı (.env veya ortam değişkeni)")
        return _save(log, 2)
    step("anahtar", True, mesaj="bulundu (değer gösterilmez)")

    try:
        models = client.list_models()
        step("model listesi", client.model in models, istenen=client.model,
             benzerleri=[m for m in models if "flash" in m][:12])
    except BridgeError as e:
        step("model listesi", False, kod=e.code, mesaj=e.user_message, detay=e.detail)
        return _save(log, 3)

    data = json.loads(Path(args.content).read_text(encoding="utf-8"))
    data.pop("_note", None)
    lesson = LessonContent.model_validate(data)
    req, _, _ = check_request(lesson.source_text, lesson.selected_phrase, lesson.subject_label)

    try:
        t0 = time.perf_counter()
        bridge = generate_bridge(req, client)
        step("generate_bridge", True, sure_sn=round(time.perf_counter() - t0, 2),
             meta=vars(client.last_meta) if client.last_meta else None, sonuc=bridge.model_dump())
    except BridgeError as e:
        step("generate_bridge", False, kod=e.code, mesaj=e.user_message, detay=e.detail)
        return _save(log, 4)

    if bridge.quiz is None:
        step("evaluate_attempt", False, mesaj="status=insufficient_source; soru üretilmedi")
        return _save(log, 5)

    right = bridge.quiz.correct_option_id
    wrong = next(o.id for o in bridge.quiz.options if o.id != right)
    for label, opt, why in (("doğru", right, lesson.correct_rationale or "Kaynaktaki kurala göre bu sonuç çıkar."),
                            ("yanlış", wrong, lesson.incorrect_rationale or "Sanırım bu doğru.")):
        try:
            t0 = time.perf_counter()
            fb = evaluate_attempt(req, bridge, opt, why, client)
            step(f"evaluate_attempt ({label})", fb.is_correct == (opt == right),
                 sure_sn=round(time.perf_counter() - t0, 2), secim=opt, sonuc=fb.model_dump())
        except BridgeError as e:
            step(f"evaluate_attempt ({label})", False, kod=e.code, mesaj=e.user_message, detay=e.detail)
    return _save(log, 0 if all(s["ok"] for s in log["steps"]) else 6)


def _save(log: dict, code: int) -> int:
    out = ROOT / "tech_logs"
    out.mkdir(exist_ok=True)
    path = out / f"api_check_{datetime.now():%Y%m%d_%H%M%S}.json"
    path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nKayıt: {path.relative_to(ROOT)}  (çıkış kodu {code})")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
