from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vector_db(chunks):

    texts = [c["content"] for c in chunks]
    metadata = [{"page": c["page"]} for c in chunks]

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=OpenAIEmbeddings(),
        metadatas=metadata,
        persist_directory="db"
    )

    vectordb.persist()

    return vectordb