import os

from dotenv import load_dotenv
from google import genai

from prompts.system_prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(question, mode, level, style, detail):

    prompt = f"""
{SYSTEM_PROMPT}

Mode belajar:
{mode}

Tingkat pendidikan:
{level}

Gaya bahasa:
{style}

Tingkat detail:
{detail}

Pertanyaan:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text