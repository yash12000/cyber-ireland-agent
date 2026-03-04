from extract_pdf import extract_text
from chunking import chunk_documents
from load_vector_db import create_vector_db


def run():

    print("Starting ETL pipeline...")

    pages = extract_text()

    print(f"Extracted {len(pages)} pages")

    chunks = chunk_documents(pages)

    print(f"Created {len(chunks)} chunks")

    create_vector_db(chunks)

    print("Vector database created successfully")


if __name__ == "__main__":
    run()