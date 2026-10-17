"""Görüntüleme bileşenleri. Kullanıcı metni HTML olarak işlenmez; kod çalıştırılmaz."""
from __future__ import annotations

import re

import streamlit as st

from core.contracts import AttemptFeedback, BridgeResult
from core.services import DEV_LABEL
from core.source import Segment, UnclosedCodeFence, split_source

_MD_SPECIAL = re.compile(r"([\\`*_{}\[\]()#+\-.!|<>~$])")
_MATH = re.compile(r"\$\$(.+?)\$\$|\\\[(.+?)\\\]|\\\((.+?)\\\)|(?<!\\)\$([^$\n]+)(?<!\\)\$", re.DOTALL)


def md_escape(text: str) -> str:
    """Düz metni markdown yorumlamadan göstermek için kaçışlar; satır sonlarını korur."""
    return _MD_SPECIAL.sub(r"\\\1", text).replace("\n", "  \n")


def _render_prose(text: str) -> None:
    """Düzyazıyı kaçırır; açık matematik işaretlerini güvenli matematik görünümüne verir."""
    cursor = 0
    for match in _MATH.finditer(text):
        before = text[cursor:match.start()]
        if before.strip():
            st.markdown(md_escape(before))
        formula = next(group for group in match.groups() if group is not None)
        st.latex(formula.strip())
        cursor = match.end()
    if text[cursor:].strip():
        st.markdown(md_escape(text[cursor:]))


def render_learning_text(text: str) -> None:
    """Kod bloklarını gösterir, çalıştırmaz. Diğer metin HTML olarak işlenmez."""
    try:
        segments = split_source(text)
    except UnclosedCodeFence:
        st.markdown(md_escape(text))
        return
    for segment in segments:
        if segment.kind == "code":
            st.code(segment.text, language=segment.lang or "python")
        else:
            _render_prose(segment.text)


def dev_banner() -> None:
    st.warning(f"**{DEV_LABEL}**", icon="🧪")


def render_source(segments: list[Segment], refs: list[str]) -> None:
    ref_set = set(refs)
    with st.expander("Kaynak metin (parça kimlikleriyle)", expanded=True):
        for seg in segments:
            mark = " — açıklamada kullanıldı" if seg.id in ref_set else ""
            st.caption(f"**{seg.id}**{mark}")
            if seg.kind == "code":
                st.code(seg.text, language=seg.lang or "python")
            else:
                _render_prose(seg.text)


def render_bridge(bridge: BridgeResult) -> None:
    if bridge.status == "insufficient_source":
        st.info(md_escape(bridge.simple_explanation), icon="ℹ️")
        for w in bridge.warnings:
            st.warning(md_escape(w))
        return

    st.subheader("Sade açıklama")
    render_learning_text(bridge.simple_explanation)
    if bridge.source_refs:
        st.caption("Dayandığı kaynak parçaları: " + ", ".join(bridge.source_refs))

    if bridge.terms:
        st.subheader("Terim kartları")
        cols = st.columns(min(len(bridge.terms), 2))
        for i, t in enumerate(bridge.terms):
            with cols[i % len(cols)]:
                with st.container(border=True):
                    st.markdown(f"**{md_escape(t.term)}**")
                    st.caption("Kaynakta geçiyor" if t.origin == "source" else "Destekleyici terim (kaynakta yok)")
                    render_learning_text(t.explanation)

    if bridge.example:
        st.subheader("Ek örnek")
        with st.container(border=True):
            st.caption("Yapay zekâ tarafından üretildi — kaynakta yer almıyor")
            render_learning_text(bridge.example.text)

    for w in bridge.warnings:
        st.warning(md_escape(w))


def render_feedback(fb: AttemptFeedback, answer_explanation: str) -> None:
    if fb.is_correct:
        st.success("Doğru seçenek.", icon="✅")
    else:
        st.error("Bu seçenek doğru değil. İpucuyla yeniden deneyebilirsiniz.", icon="✖️")
    if fb.strengths:
        st.markdown("**Gerekçenizde iyi olanlar**")
        for s in fb.strengths:
            st.markdown("- " + md_escape(s))
    if fb.improvements:
        st.markdown("**Geliştirilebilecekler**")
        for s in fb.improvements:
            st.markdown("- " + md_escape(s))
    if fb.retry_hint:
        st.info(md_escape(fb.retry_hint), icon="💡")
    if fb.is_correct:
        st.caption("Neden doğru: " + md_escape(answer_explanation))
    else:
        with st.expander("Doğru cevabı göster"):
            render_learning_text(answer_explanation)
