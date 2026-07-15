from dataclasses import dataclass
from typing import Any

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class RagIndex:
    chunks: list[dict[str, object]]
    vectorizer: TfidfVectorizer
    document_matrix: Any


def split_text(
    text: str,
    chunk_size: int = 1200,
    overlap: int = 200,
) -> list[str]:
    """
    Memecah teks menjadi chunk dengan overlap.

    chunk_size dan overlap dihitung dalam karakter.
    """
    cleaned_text = " ".join(text.split())

    if not cleaned_text:
        return []

    chunks: list[str] = []
    start = 0
    text_length = len(cleaned_text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start = max(end - overlap, start + 1)

    return chunks


def build_rag_index(
    pages: list[dict[str, object]],
) -> RagIndex | None:
    """
    Membuat indeks TF-IDF dari teks PDF.
    """
    chunks: list[dict[str, object]] = []

    for page_data in pages:
        page_number = int(page_data["page"])
        page_text = str(page_data["text"])

        page_chunks = split_text(page_text)

        for chunk_number, chunk_text in enumerate(
            page_chunks,
            start=1,
        ):
            chunks.append(
                {
                    "page": page_number,
                    "chunk": chunk_number,
                    "text": chunk_text,
                }
            )

    if not chunks:
        return None

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        max_features=30_000,
    )

    document_matrix = vectorizer.fit_transform(
        [str(chunk["text"]) for chunk in chunks]
    )

    return RagIndex(
        chunks=chunks,
        vectorizer=vectorizer,
        document_matrix=document_matrix,
    )


def retrieve_relevant_chunks(
    query: str,
    rag_index: RagIndex | None,
    top_k: int = 4,
    minimum_score: float = 0.03,
) -> list[dict[str, object]]:
    """
    Mengambil chunk PDF yang paling relevan dengan pertanyaan.
    """
    if rag_index is None or not query.strip():
        return []

    query_vector = rag_index.vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector,
        rag_index.document_matrix,
    ).flatten()

    ranked_indices = np.argsort(scores)[::-1]

    results: list[dict[str, object]] = []

    for index in ranked_indices:
        score = float(scores[index])

        if score < minimum_score:
            continue

        chunk = rag_index.chunks[int(index)].copy()
        chunk["score"] = score
        results.append(chunk)

        if len(results) >= top_k:
            break

    return results


def format_context(
    retrieved_chunks: list[dict[str, object]],
) -> str:
    """
    Membuat konteks yang siap dimasukkan ke prompt Gemini.
    """
    if not retrieved_chunks:
        return ""

    context_parts: list[str] = []

    for item in retrieved_chunks:
        page = item["page"]
        text = item["text"]

        context_parts.append(
            f"[Sumber: halaman {page}]\n{text}"
        )

    return "\n\n---\n\n".join(context_parts)