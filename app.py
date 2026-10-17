"""Anlatım Köprüsü — Streamlit uygulaması.

Çalıştırma:  streamlit run app.py
"""
from __future__ import annotations

import logging
import os

import streamlit as st

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv yoksa ortam değişkenleri doğrudan kullanılır
    pass

from core.content_loader import load_lessons
from core.contracts import BridgeError
from core.gemini_client import DEFAULT_MODEL
from core.services import check_request, evaluate_attempt, generate_bridge, prompt_version
from ui import state as S
from ui.views import dev_banner, render_bridge, render_feedback, render_learning_text, render_source

log = logging.getLogger("anlatim_koprusu")
OWN_TEXT = "✍️ Kendi metnim"
MODE_LIVE, MODE_DEV = "Canlı (Gemini)", "Geliştirme verisi"

st.set_page_config(page_title="Anlatım Köprüsü", page_icon="🌉", layout="wide")

# ---------------------------------------------------------------- içerik
report = load_lessons()
lessons = {l.title: l for l in report.lessons}


def _apply_lesson() -> None:
    choice = st.session_state.get("lesson_choice")
    if choice in lessons:
        l = lessons[choice]
        st.session_state["source_text"] = l.source_text
        st.session_state["phrase"] = l.selected_phrase
        st.session_state["subject"] = l.subject_label
    else:
        st.session_state["source_text"] = ""
        st.session_state["phrase"] = ""
        st.session_state["subject"] = ""


if "lesson_choice" not in st.session_state:
    st.session_state["lesson_choice"] = next(iter(lessons))
    _apply_lesson()

# ---------------------------------------------------------------- kenar çubuğu
with st.sidebar:
    st.header("Ayarlar")
    mode = st.radio("Çalışma modu", [MODE_LIVE, MODE_DEV], key="mode")
    dev_kind = None
    if mode == MODE_DEV:
        dev_kind = st.selectbox("Geliştirme sonucu", ["ready", "insufficient_source"], key="dev_kind")
        st.caption("Model çağrılmaz; etiketli örnek veri gösterilir.")
    else:
        has_key = bool(os.getenv("GEMINI_API_KEY", "").strip())
        st.caption(f"Model: `{os.getenv('GEMINI_MODEL') or DEFAULT_MODEL}` · Prompt: `{prompt_version()}`")
        if has_key:
            st.caption("API anahtarı: bulundu ✓")
        else:
            st.warning("GEMINI_API_KEY bulunamadı. README'deki adımlarla .env dosyasını hazırlayın "
                       "ya da Geliştirme verisi moduna geçin.")
    if report.using_dev_input:
        st.info("content/ klasöründe ders bulunamadı; geliştirme taslağı gösteriliyor.")
    for err in report.errors:
        st.error(f"İçerik dosyası okunamadı — {err}")

# ---------------------------------------------------------------- girdiler (form DIŞINDA)
st.title("🌉 Anlatım Köprüsü")
st.caption("Zorlandığın akademik ifadeyi kaynağına bağlı kalarak adım adım anla.")

st.selectbox("Metin", list(lessons) + [OWN_TEXT], key="lesson_choice", on_change=_apply_lesson)
is_own = st.session_state["lesson_choice"] == OWN_TEXT
st.text_input("Ders / konu etiketi (isteğe bağlı)", key="subject", max_chars=80, disabled=not is_own)
st.text_area("Kaynak metin", key="source_text", height=260, max_chars=6000,
             help="Kod parçalarını ``` satırları arasına alın. Yapıştırılan kod çalıştırılmaz.")
st.text_input("Zorlandığın ifade (kaynaktan kopyala)", key="phrase", max_chars=500)

source_text = st.session_state["source_text"]
phrase = st.session_state["phrase"]
subject = st.session_state["subject"] or None
fp = S.fingerprint(source_text, phrase, subject)
generation_context = (mode, dev_kind, prompt_version(), os.getenv("GEMINI_MODEL") or DEFAULT_MODEL)
previous_context = st.session_state.get("generation_context")
if previous_context is not None and previous_context != generation_context:
    S.clear_work(st.session_state)
st.session_state["generation_context"] = generation_context
S.sync_work(st.session_state, fp)  # girdi değiştiyse eski çalışmayı temizle

explain_clicked = st.button("Açıkla", type="primary")

if explain_clicked:
    try:
        req, _, _ = check_request(source_text, phrase, subject)
        with st.spinner("Açıklama hazırlanıyor…"):
            bridge = generate_bridge(req, dev_fixture=dev_kind)
        S.store_bridge(st.session_state, fp, req, bridge, is_dev=dev_kind is not None)
    except BridgeError as e:
        log.warning("generate_bridge %s %s", e.code, e.detail)
        st.error(e.user_message)  # aynı girdideki önceki başarılı sonuç korunur

# ---------------------------------------------------------------- sonuç
work = S.current_work(st.session_state, fp)
if work is not None:
    bridge = work["bridge"]
    if work["is_dev"]:
        dev_banner()
    source_column, explanation_column = st.columns(2)
    with source_column:
        try:
            _, segments, _ = check_request(source_text, phrase, subject)
            render_source(segments, bridge.source_refs)
        except BridgeError:
            pass
    with explanation_column:
        render_bridge(bridge)

    if bridge.status == "ready" and bridge.quiz is not None:
        quiz = bridge.quiz
        st.subheader("Kendini dene")
        render_learning_text(quiz.question)
        texts = {o.id: o.text for o in quiz.options}
        nonce = st.session_state.get(S.NONCE, 0)
        with st.form(key=f"answer_form_{nonce}"):
            choice = st.radio("Cevabın", list(texts), index=None, key=f"choice_{nonce}",
                              format_func=lambda i: f"{i}) {texts[i]}")
            rationale = st.text_area("Neden bu seçeneği seçtin? (kısa gerekçe)", key=f"rationale_{nonce}",
                                     max_chars=1000, height=100)
            submitted = st.form_submit_button("Cevabı gönder")
        if submitted:
            if rationale and 0 < len(rationale.split()) < 3:
                st.info("Gerekçen çok kısa görünüyor; birkaç kelimeyle nedenini açıklarsan geri bildirim daha işe yarar olur.")
            try:
                with st.spinner("Geri bildirim hazırlanıyor…"):
                    fb = evaluate_attempt(work["request"], bridge, choice, rationale, dev=work["is_dev"])
                S.store_feedback(st.session_state, fp, fb, choice)
            except BridgeError as e:
                log.warning("evaluate_attempt %s %s", e.code, e.detail)
                st.error(e.user_message)

        fb_state = S.current_feedback(st.session_state, fp)
        if fb_state is not None:
            if work["is_dev"]:
                dev_banner()
            render_feedback(fb_state["feedback"], quiz.answer_explanation)
            if st.button("Tekrar dene"):
                S.reset_answer(st.session_state)
                st.rerun()
            st.caption("Yeni soru için yukarıdaki **Açıkla** düğmesine yeniden basabilirsin.")
