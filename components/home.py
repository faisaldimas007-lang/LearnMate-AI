import streamlit as st


def render_home():
    st.markdown("## 👋 Apa yang ingin kamu pelajari hari ini?")

    st.caption(
        "Pilih salah satu menu cepat atau tuliskan pertanyaanmu langsung."
    )

    col1, col2 = st.columns(2)

    quick_prompt = None

    with col1:
        if st.button(
            "📖 Jelaskan Materi",
            use_container_width=True,
        ):
            quick_prompt = "Jelaskan materi tentang "

        if st.button(
            "❓ Buat Quiz",
            use_container_width=True,
        ):
            quick_prompt = "Buatkan quiz tentang "

        if st.button(
            "💻 Belajar Python",
            use_container_width=True,
        ):
            quick_prompt = "Ajarkan saya dasar-dasar Python."

    with col2:
        if st.button(
            "📝 Ringkas Materi",
            use_container_width=True,
        ):
            quick_prompt = "Ringkas materi tentang "

        if st.button(
            "📅 Buat Study Planner",
            use_container_width=True,
        ):
            quick_prompt = "Buatkan rencana belajar untuk "

        if st.button(
            "📊 Belajar Statistika",
            use_container_width=True,
        ):
            quick_prompt = "Jelaskan konsep dasar statistika."

    return quick_prompt