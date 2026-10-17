"""Görüntüleme bileşenleri. Kullanıcı metni HTML olarak işlenmez; kod çalıştırılmaz."""
from __future__ import annotations

import re

import streamlit as st

from core.contracts import AttemptFeedback, BridgeResult
from core.services import DEV_LABEL
from core.source import Segment

_MD_SPECIAL = re.compile(r"([\\`*_{}\[\]()#+\-.!|<>~$])")


def md_escape(text: str) -> str:
    """Düz metni markdown yorumlamadan göstermek için kaçışlar; satır sonlarını korur."""
    return _MD_SPECIAL.sub(r"\\\1", text).replace("\n", "  \n")


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
                st.markdown(md_escape(seg.text))


def render_bridge(bridge: BridgeResult) -> None:
    if bridge.status == "insufficient_source":
        st.info(md_escape(bridge.simple_explanation), icon="ℹ️")
        for w in bridge.warnings:
            st.warning(md_escape(w))
        return

    st.subheader("Sade açıklama")
    st.markdown(md_escape(bridge.simple_explanation))
    if bridge.source_refs:
        st.caption("Dayandığı kaynak parçaları: " + ", ".join(bridge.source_refs))

    if bridge.terms:
        st.subheader("Terim kartları")
        cols = st.columns(min(len(bridge.terms), 3))
        for i, t in enumerate(bridge.terms):
            with cols[i % len(cols)]:
                with st.container(border=True):
                    st.markdown(f"**{md_escape(t.term)}**")
                    st.caption("Kaynakta geçiyor" if t.origin == "source" else "Destekleyici terim (kaynakta yok)")
                    st.write(md_escape(t.explanation))

    if bridge.example:
        st.subheader("Ek örnek")
        with st.container(border=True):
            st.caption("Yapay zekâ tarafından üretildi — kaynakta yer almıyor")
            st.markdown(md_escape(bridge.example.text))

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
            st.markdown(md_escape(answer_explanation))
