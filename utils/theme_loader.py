from pathlib import Path

import streamlit as st


THEME_FILES = {
    "🌞 Light": "assets/themes/light.css",
    "🌙 Dark": "assets/themes/dark.css",
    "🌊 Ocean": "assets/themes/ocean.css",
    "💜 Purple": "assets/themes/purple.css",
}


def load_css_file(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")


def load_theme(theme_name: str) -> None:
    base_css = load_css_file("assets/style.css")

    theme_path = THEME_FILES.get(
        theme_name,
        THEME_FILES["🌞 Light"],
    )

    theme_css = load_css_file(theme_path)

    st.markdown(
        f"""
        <style>
        {theme_css}
        {base_css}
        </style>
        """,
        unsafe_allow_html=True,
    )