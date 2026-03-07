from langchain_text_splitters import RecursiveCharacterTextSplitter
import re


def clean_text(text):

    if text is None:
        return ""

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"\b\d{1,2}\b", "", text)

    return text.strip()


def chunk_documents(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=120
    )

    chunks = []

    for page in pages:

        cleaned = clean_text(page["text"])

        page_chunks = splitter.split_text(cleaned)

        for chunk in page_chunks:

            chunks.append({
                "content": chunk,
                "page": page["page"]
            })

    return chunks