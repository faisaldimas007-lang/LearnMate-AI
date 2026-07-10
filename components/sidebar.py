import streamlit as st


def render_sidebar():
    st.sidebar.title("🎓 LearnMate AI")

    mode = st.sidebar.selectbox(
        "📚 Mode Belajar",
        [
            "📖 Penjelasan Materi",
            "📝 Ringkasan",
            "❓ Quiz Generator",
            "📅 Study Planner",
            "💻 Belajar Coding",
            "📊 Data Science Assistant",
        ],
    )

    level = st.sidebar.selectbox(
        "🎓 Tingkat Pendidikan",
        ["SMP", "SMA", "Mahasiswa"],
    )

    style = st.sidebar.selectbox(
        "🗣️ Gaya Bahasa",
        ["Santai", "Formal"],
    )

    detail = st.sidebar.selectbox(
        "📏 Tingkat Detail",
        ["Singkat", "Sedang", "Lengkap"],
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader("📈 Dashboard")

    messages = st.session_state.get("messages", [])

    total_chat = sum(
        1 for message in messages
        if message.get("role") == "user"
    )

    st.sidebar.metric("💬 Total Chat", total_chat)
    st.sidebar.metric(
        "📄 PDF Dibaca",
        st.session_state.get("pdf_count", 0),
    )
    st.sidebar.metric(
        "📝 Quiz Dibuat",
        st.session_state.get("quiz_count", 0),
    )

    if st.sidebar.button(
        "🗑️ Hapus Riwayat",
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.rerun()

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
🎯 **LearnMate AI**

Asisten belajar berbasis Gemini AI.

"""
    )

    st.sidebar.caption(
        "Developed with ❤️ by Dimas Faisal Zulmi"
    )

    return mode, level, style, detail