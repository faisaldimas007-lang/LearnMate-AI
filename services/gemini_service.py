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
    pdf_text=""
):

    prompt = f"""
{SYSTEM_PROMPT}

MODE:
{mode}

TINGKAT:
{level}

STYLE:
{style}

DETAIL:
{detail}

======================

Materi PDF:

{pdf_text}

======================

Pertanyaan:

{question}

Jika terdapat isi PDF, prioritaskan menjawab berdasarkan isi PDF.
Jika tidak ada informasi yang relevan di PDF, jelaskan bahwa jawabannya berasal dari pengetahuan umum.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text