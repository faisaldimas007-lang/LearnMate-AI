import streamlit as st

from components.chat import add_message, display_chat
from components.csv_viewer import render_csv_viewer
from components.home import render_home
from components.sidebar import render_sidebar
from components.uploaders import render_uploaders
from services.gemini_service import ask_gemini
from utils.style_loader import load_css

st.set_page_config(
    page_title="LearnMate AI",
    page_icon="🎓",
    layout="wide",
)

load_css("assets/style.css")

st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        font-size: 2.4rem !important;
        margin-bottom: 0.2rem !important;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 44px;
    }

    div[data-testid="stChatInput"] {
        border-radius: 12px;
    }

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 0.5rem;
        margin-bottom: 0.6rem;
    }

    div[data-testid="stMetric"] {
        border: 1px solid rgba(128, 128, 128, 0.2);
        padding: 10px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
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

# Upload
pdf_text, dataframe = render_uploaders()

# Header
st.markdown(
    """
    <div class="hero">
        <p class="hero-title">🎓 LearnMate AI</p>
        <p class="hero-subtitle">
            Asisten belajar berbasis Gemini AI yang membantu proses belajar
            menjadi mudah dan menyenangkan.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# CSV
render_csv_viewer(dataframe)

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