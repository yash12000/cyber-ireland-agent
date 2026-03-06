from etl.extract_pdf import extract_text
from etl.parse_tables import extract_tables
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db


def run_pipeline():

    print("Extracting PDF text...")
    pages = extract_text()

    print("Extracting tables...")
    tables = extract_tables()

    print("Chunking documents...")
    chunks = chunk_documents(pages)

    print("Creating vector database...")
    vectordb = create_vector_db(chunks)

    print("Pipeline complete!")
    print(f"Pages processed: {len(pages)}")
    print(f"Tables extracted: {len(tables)}")
    print(f"Chunks created: {len(chunks)}")


if __name__ == "__main__":
    run_pipeline()