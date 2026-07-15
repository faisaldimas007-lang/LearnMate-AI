import streamlit as st

from services.rag_service import build_rag_index
from utils.csv_reader import read_csv
from utils.pdf_reader import extract_pdf_pages


def render_uploaders():
    uploaded_pdf = st.sidebar.file_uploader(
        "📄 Upload Materi PDF",
        type=["pdf"],
        key="pdf_uploader",
    )

    uploaded_csv = st.sidebar.file_uploader(
        "📊 Upload Dataset CSV",
        type=["csv"],
        key="csv_uploader",
    )

    dataframe = None

    if uploaded_pdf is not None:
        current_pdf_name = uploaded_pdf.name
        previous_pdf_name = st.session_state.get(
            "last_pdf_name"
        )

        # PDF hanya diproses ulang jika file berubah.
        if current_pdf_name != previous_pdf_name:
            with st.sidebar:
                with st.spinner("Membuat indeks PDF..."):
                    pages = extract_pdf_pages(uploaded_pdf)
                    rag_index = build_rag_index(pages)

                    st.session_state.rag_index = rag_index
                    st.session_state.pdf_page_count = len(pages)
                    st.session_state.last_pdf_name = (
                        current_pdf_name
                    )
                    st.session_state.pdf_count += 1

        if st.session_state.get("rag_index") is not None:
            page_count = st.session_state.get(
                "pdf_page_count",
                0,
            )

            st.sidebar.success(
                f"✅ PDF siap digunakan ({page_count} halaman)."
            )
        else:
            st.sidebar.warning(
                "PDF tidak menghasilkan teks yang dapat dibaca."
            )

    else:
        # Hapus indeks jika pengguna menghapus file dari uploader.
        st.session_state.rag_index = None
        st.session_state.last_pdf_name = None
        st.session_state.pdf_page_count = 0

    if uploaded_csv is not None:
        dataframe = read_csv(uploaded_csv)

    return dataframe