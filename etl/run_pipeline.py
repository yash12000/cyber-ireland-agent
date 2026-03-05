from etl.extract_pdf import extract_text
from etl.chunking import chunk_documents
from etl.load_vector_db import create_vector_db

print("Extracting PDF...")
pages = extract_text()

print("Chunking text...")
chunks = chunk_documents(pages)

print("Creating vector database...")
create_vector_db(chunks)

print("Pipeline completed.")