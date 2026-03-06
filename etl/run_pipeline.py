from extract_pdf import extract_text
from chunking import chunk_documents
from load_vector_db import create_vector_db


def run_pipeline():

    print("Step 1: Extracting text from PDF...")
    pages = extract_text()

    print(f"Extracted {len(pages)} pages")

    print("Step 2: Chunking documents...")
    chunks = chunk_documents(pages)

    print(f"Created {len(chunks)} chunks")

    print("Step 3: Creating vector database...")
    vectordb = create_vector_db(chunks)

    print("Vector DB created successfully")


if __name__ == "__main__":
    run_pipeline()