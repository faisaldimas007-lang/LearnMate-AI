from pathlib import Path

import streamlit as st


def load_css(file_path: str) -> None:
    css_path = Path(file_path)

    if not css_path.exists():
        return

    css_content = css_path.read_text(encoding="utf-8")

    st.markdown(
        f"<style>{css_content}</style>",
        unsafe_allow_html=True,
    )