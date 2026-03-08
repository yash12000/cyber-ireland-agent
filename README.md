# Cyber Ireland Agentic RAG Backend

## Overview

This project implements an **agentic Retrieval-Augmented Generation (RAG) backend** that converts the **Cyber Ireland 2022 Report** into a dynamic, queryable knowledge system.

Unlike a basic RAG system, this solution introduces **autonomous agent orchestration**, enabling the system to:

* Retrieve relevant information from the PDF
* Perform multi-step reasoning
* Execute mathematical calculations using tools
* Provide verifiable citations from the document

The system exposes a **FastAPI endpoint** that accepts natural language queries and returns grounded answers based on the report.

---

# Architecture

The system follows a **four-layer architecture**:

```
User Query
     │
     ▼
FastAPI Backend (/query)
     │
     ▼
Agent Orchestrator (LangChain Agent)
     │
 ┌───────┬────────┐
 ▼       ▼        ▼
Retriever  Math Tool  Document Parser
(Vector DB)
     │
     ▼
Chroma Vector Database
     │
     ▼
Parsed PDF + Tables
```

---

# Technology Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Backend API      | FastAPI           |
| Agent Framework  | LangChain         |
| Vector Database  | ChromaDB          |
| Embeddings       | OpenAI Embeddings |
| PDF Parsing      | pdfplumber        |
| Table Extraction | Camelot           |
| Observability    | LangSmith         |
| Math Tool        | Python            |

---

# Project Structure

```
cyber-ireland-agent
│
├── app
│   ├── main.py          
│   ├── agent.py         
│   ├── retriever.py     
│   └── tools.py         
│
├── etl
│   ├── extract_pdf.py   
│   ├── parse_tables.py  
│   ├── chunking.py      
│   └── load_vector_db.py
│
├── data
│   ├── raw              
│   └── processed        
│
├── db                   
├── logs                 
├── tests                
│
├── requirements.txt
├── README.md
└── .env
```

---

# Setup Instructions

## 1. Clone Repository

```
git clone https://github.com/yash12000/cyber-ireland-agent
cd cyber-ireland-agent
```

---

## 2. Create Virtual Environment

Windows

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
```

---

## 5. Add the Source PDF

Place the report inside:

```
data/raw/cyber_security_report.pdf
```

---

# ETL Pipeline

The ETL pipeline processes the PDF into structured data suitable for retrieval.

### Step 1 — Extract Text

```
python etl/extract_pdf.py
```

Extracts text from every page of the report.

---

### Step 2 — Extract Tables

```
python etl/parse_tables.py
```

Parses structured tables from the report.

---

### Step 3 — Chunk Documents

Splits large text into semantic chunks for embedding.

---

### Step 4 — Build Vector Database

```
python etl/load_vector_db.py
```

Creates a Chroma vector store for semantic retrieval.

---

# Running the Backend

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

### POST `/query`

Example request:

```
{
  "question": "What is the total number of jobs reported?"
}
```

Example response:

```
{
  "query": "What is the total number of jobs reported?",
  "answer": "The report states that the sector employs 7,351 cyber security professionals in Ireland."
}
```

The system retrieves the supporting citation from the report.

---

# Evaluation Queries

The system is designed to handle the following evaluation scenarios.

---

## Test 1 — Verification Challenge

Query:

```
What is the total number of jobs reported, and where exactly is this stated?
```

Expected behavior:

* Retrieve the job count
* Provide the page citation

---

## Test 2 — Data Synthesis Challenge

Query:

```
Compare the concentration of Pure-Play cybersecurity firms in the South-West against the national average.
```

Agent behavior:

1. Retrieve regional firm distribution tables
2. Extract pure-play metrics
3. Perform comparative analysis

---

## Test 3 — Forecasting Challenge

Query:

```
Based on our 2022 baseline and the 2030 job target, what CAGR is required?
```

Agent behavior:

1. Retrieve baseline employment
2. Retrieve 2030 job target
3. Use calculator tool
4. Return CAGR value

---

# Execution Traces

Agent reasoning can be inspected via **LangSmith traces**, which show:

* Retrieval steps
* Tool usage
* Intermediate reasoning
* Final answer generation

---

# Architecture Justification

### ETL Strategy

`pdfplumber` and `Camelot` were selected because the report contains both narrative text and structured data tables.

### Vector Database

ChromaDB was chosen due to:

* Lightweight deployment
* Local persistence
* Efficient semantic retrieval

### Agent Framework

LangChain agents enable:

* Tool execution
* Multi-step reasoning
* Observability via LangSmith

---

# Limitations

Current limitations include:

* Table parsing may require additional cleaning
* Retrieval accuracy depends on chunking strategy
* System assumes a single PDF knowledge source

---

# Future Improvements

Potential improvements include:

* Hybrid search (BM25 + vector retrieval)
* Multi-document support
* Graph-based knowledge indexing
* Distributed vector database (Pinecone / Weaviate)

---

# Author

Yash Janbandhu
Assignment Submission – Agentic RAG Backend
