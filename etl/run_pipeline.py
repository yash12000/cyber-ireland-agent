from .extract_pdf import extract_text
from .chunking import chunk_documents
from .load_vector_db import create_vector_db


def run_pipeline():

    pages = extract_text()

    chunks = chunk_documents(pages)

    create_vector_db(chunks)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()