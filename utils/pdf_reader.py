from typing import Any

from pypdf import PdfReader


def extract_pdf_pages(uploaded_file: Any) -> list[dict[str, object]]:
    """
    Mengekstrak teks PDF per halaman.

    Return:
        [
            {
                "page": 1,
                "text": "Isi halaman..."
            }
        ]
    """
    reader = PdfReader(uploaded_file)
    pages: list[dict[str, object]] = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        page_text = " ".join(page_text.split())

        if page_text.strip():
            pages.append(
                {
                    "page": page_number,
                    "text": page_text,
                }
            )

    return pages