from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def get_retriever():

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever