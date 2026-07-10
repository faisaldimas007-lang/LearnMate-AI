import streamlit as st

from components.sidebar import render_sidebar
from services.gemini_service import ask_gemini
from components.home import render_home
from utils.pdf_reader import read_pdf
from components.chat import display_chat, add_message

st.set_page_config(
    page_title="LearnMate AI",
    page_icon="🎓",
    layout="wide"
)

# Inisialisasi session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "quiz_count" not in st.session_state:
    st.session_state.quiz_count = 0

if "pdf_count" not in st.session_state:
    st.session_state.pdf_count = 0

# Sidebar dipanggil setelah session state tersedia
mode, level, style, detail = render_sidebar()

uploaded_file = st.sidebar.file_uploader(
    "📄 Upload Materi PDF",
    type=["pdf"]
)

pdf_text = ""

if uploaded_file:
    if st.session_state.get("last_pdf_name") != uploaded_file.name:
        st.session_state.pdf_count += 1
        st.session_state.last_pdf_name = uploaded_file.name

    pdf_text = read_pdf(uploaded_file)
    st.sidebar.success("✅ PDF berhasil dibaca!")

# Header
st.title("🎓 LearnMate AI")
st.caption("AI Learning Assistant untuk membantu belajar")


# Quick action
quick_prompt = None

if len(st.session_state.messages) == 0:
    quick_prompt = render_home()

# Menyimpan riwayat chat


    st.info(
        """
👋 Selamat datang di **LearnMate AI**!

Silakan pilih mode belajar di sidebar, lalu ajukan pertanyaan.

Contoh:

- Apa itu Regresi Linear?
- Ringkas materi Peluang.
- Buatkan quiz Statistika.
- Susunkan jadwal belajar UTBK.
"""
    )    

# Menampilkan riwayat chat

display_chat()

# Input pengguna
chat_prompt = st.chat_input(
    "Tulis pertanyaanmu di sini..."
)

prompt = quick_prompt if quick_prompt else chat_prompt

if prompt:

    # Simpan pesan pengguna
    add_message("user", prompt)

    # Tampilkan pesan pengguna
    with st.chat_message("user", avatar="👨‍🎓"):
        st.markdown(prompt)

    # Meminta jawaban Gemini
    with st.chat_message("assistant", avatar="🎓"):
        try:
            with st.spinner("LearnMate sedang berpikir..."):
                response = ask_gemini(
                    prompt,
                    mode,
                    level,
                    style,
                    detail,
                    pdf_text,
                )

            if "Quiz" in mode:
                st.session_state.quiz_count += 1

            st.markdown(response)

            # Simpan jawaban AI setelah response berhasil dibuat
            add_message("assistant", response)

        except Exception as error:
            st.error(
                f"Terjadi kesalahan saat menghubungi Gemini: {error}"
            )