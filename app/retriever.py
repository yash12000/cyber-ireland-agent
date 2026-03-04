from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


def get_retriever():

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=OpenAIEmbeddings()
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever