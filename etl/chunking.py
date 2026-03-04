from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_documents(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = []

    for page in pages:

        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:

            chunks.append({
                "content": chunk,
                "page": page["page"]
            })

    return chunks