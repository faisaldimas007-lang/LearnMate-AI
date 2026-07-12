import streamlit as st

from utils.pdf_reader import read_pdf
from utils.csv_reader import read_csv


def render_uploaders():
    uploaded_pdf = st.sidebar.file_uploader(
        "📄 Upload Materi PDF",
        type=["pdf"],
    )

    uploaded_csv = st.sidebar.file_uploader(
        "📊 Upload Dataset CSV",
        type=["csv"],
    )

    pdf_text = ""
    dataframe = None

    if uploaded_pdf is not None:
        if st.session_state.get("last_pdf_name") != uploaded_pdf.name:
            st.session_state.pdf_count += 1
            st.session_state.last_pdf_name = uploaded_pdf.name

        pdf_text = read_pdf(uploaded_pdf)
        st.sidebar.success("✅ PDF berhasil dibaca!")

    if uploaded_csv is not None:
        dataframe = read_csv(uploaded_csv)

    return pdf_text, dataframe