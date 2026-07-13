import streamlit as st


def render_sidebar():
    st.sidebar.title("🎓 LearnMate AI")
    st.sidebar.caption("Personal AI Learning Assistant")

    st.sidebar.markdown("---")

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
        [
            "SMP",
            "SMA",
            "Mahasiswa",
        ],
    )

    style = st.sidebar.selectbox(
        "🗣️ Gaya Bahasa",
        [
            "Santai",
            "Formal",
        ],
    )

    detail = st.sidebar.selectbox(
        "📏 Tingkat Detail",
        [
            "Singkat",
            "Sedang",
            "Lengkap",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader("📈 Aktivitas")

    messages = st.session_state.get("messages", [])

    total_chat = sum(
        1
        for message in messages
        if message.get("role") == "user"
    )

    col1, col2 = st.sidebar.columns(2)

    with col1:
        st.metric(
            "Chat",
            total_chat,
        )

    with col2:
        st.metric(
            "Quiz",
            st.session_state.get("quiz_count", 0),
        )

    st.sidebar.metric(
        "PDF",
        st.session_state.get("pdf_count", 0),
    )

    if st.sidebar.button(
        "🗑️ Hapus Riwayat",
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.caption("Dibuat oleh Dimas Faisal Zulmi")

    return mode, level, style, detail