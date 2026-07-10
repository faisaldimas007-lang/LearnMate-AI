import streamlit as st

from components.sidebar import render_sidebar
from services.gemini_service import ask_gemini


st.set_page_config(
    page_title="LearnMate AI",
    page_icon="🎓",
    layout="wide"
)

mode, level, style, detail = render_sidebar()

st.logo("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

st.title("🎓 LearnMate AI")

st.caption("AI Learning Assistant untuk membantu belajar") 

# Menyimpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
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
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input pengguna
prompt = st.chat_input("Tulis pertanyaanmu di sini...")

if prompt:

    # Simpan pesan pengguna
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(prompt)

    # Minta jawaban Gemini
    with st.chat_message("assistant"):

        with st.spinner("LearnMate sedang berpikir..."):

            response = ask_gemini(
                prompt,
                mode,
                level,
                style,
                detail
              )

        st.markdown(response)

    # Simpan jawaban AI
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )