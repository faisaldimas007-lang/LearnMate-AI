import streamlit as st

def render_sidebar():

    st.sidebar.title("🎓 LearnMate AI")

    mode = st.sidebar.selectbox(
        "📚 Mode Belajar",
        [
            "Penjelasan Materi",
            "Ringkasan",
            "Quiz Generator",
            "Study Planner"
        ]
    )

    level = st.sidebar.selectbox(
        "🎓 Tingkat Pendidikan",
        [
            "SMP",
            "SMA",
            "Mahasiswa"
        ]
    )

    style = st.sidebar.selectbox(
        "🗣️ Gaya Bahasa",
        [
            "Santai",
            "Formal"
        ]
    )

    detail = st.sidebar.selectbox(
        "📏 Tingkat Detail",
        [
            "Singkat",
            "Sedang",
            "Lengkap"
        ]
    )
    st.sidebar.markdown("---")
    st.sidebar.metric(
    "💬 Total Percakapan",
    len(st.session_state.messages)
    )   

    st.sidebar.info(
         """
            🎯 **LearnMate AI**

            Asisten belajar berbasis Gemini AI.

            Dibuat oleh:
            **Dimas Faisal Zulmi**
            """
    )


    return mode, level, style, detail

if st.sidebar.button("🗑 Hapus Riwayat"):

    st.session_state.messages = []

    st.rerun()

    st.sidebar.markdown("---")

st.sidebar.caption(
    "Developed with ❤️ by Dimas Faisal Zulmi"
)