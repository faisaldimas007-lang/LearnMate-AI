from google import genai
from dotenv import load_dotenv
import os
import streamlit as st

print("===== GEMINI SERVICE LOADED =====")
print(__file__)

from prompts.system_prompt import SYSTEM_PROMPT

load_dotenv()

def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        return os.getenv("GEMINI_API_KEY")


api_key = get_api_key()

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY belum dikonfigurasi."
    )

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(
    question,
    mode,
    level,
    style,
    detail,
    pdf_context="",
):

    prompt = f"""
{SYSTEM_PROMPT}

MODE BELAJAR:
{mode}

TINGKAT PENDIDIKAN:
{level}

GAYA BAHASA:
{style}

TINGKAT DETAIL:
{detail}

========================
KONTEKS DARI DOKUMEN PDF
========================

{pdf_context if pdf_context else "Tidak ada konteks PDF yang relevan."}

========================
PERTANYAAN PENGGUNA
========================

{question}

ATURAN PENTING:

1. Jika konteks PDF tersedia, prioritaskan konteks tersebut.
2. Jangan mengarang isi dokumen yang tidak tersedia.
3. Sertakan nomor halaman saat menggunakan informasi PDF.
4. Jika konteks PDF tidak cukup untuk menjawab, katakan dengan jelas.
5. Jangan mengatakan telah membaca seluruh dokumen jika hanya menerima beberapa bagian.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text