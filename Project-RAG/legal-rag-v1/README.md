# Legal RAG v1 (Retrieval-Augmented Generation) - French

This repository implements a **minimal but realistic Legal RAG v1** for French legal text: from raw legal documents to a `/ask` API that returns **grounded, cited answers** built on BM25 + dense retrieval + cross-encoder reranking + an LLM.

The design is inspired by modern RAG architectures and tailored to a LegalTech use case (“question utilisateur → extraits pertinents → réponse fiable et sourcée”).

---

## 1. Scope & assumptions

- **Domain (v1):** Narrow subset of French legal content (e.g., selected articles from a single code or topic such as *licenciement*).
- **Language:** French input/output.
- **Goal:** Demonstrate the full pipeline:
  1. Ingestion & indexing
  2. Query understanding
  3. Hybrid retrieval
  4. Reranking
  5. Grounded generation with citations
  6. Basic evaluation

It is **not** a production system yet, but the structure is compatible with hardening and scaling.

---

## 2. High-level architecture

### 2.1 Data pipeline

- `etl/ingest_legal_corpus.py`
  Parse raw legal documents (PDF/HTML) into normalized text with base metadata (title, source, jurisdiction, dates).

- `etl/chunk_legal_docs.py`
  Chunk documents into **legally meaningful units** (articles / paragraphs where possible). Each chunk has:
  - `doc_id`, `chunk_id`
  - `article`, `section`
  - `jurisdiction`, `doc_type`, `effective_date`, `source_url`

- Outputs are stored in `data/processed/documents.parquet` and `data/processed/chunks.parquet`.

### 2.2 Indexing

- `indexing/index_bm25.py`
  - Builds a **BM25 index** (Elasticsearch/OpenSearch) over chunks.
  - Uses a French analyzer and boosts article titles/numbers for citation-style queries.

- `indexing/build_embeddings.py` + `indexing/index_vectors.py`
  - Computes dense embeddings for each chunk using a multilingual Sentence-Transformers model.
  - Stores vectors + metadata in a local **vector DB** (e.g., Qdrant/Chroma).

---

## 3. Retrieval & reranking

### 3.1 Hybrid retrieval

- `retrieval/bm25_retriever.py`
  Thin wrapper around the BM25 index.

- `retrieval/dense_retriever.py`
  Thin wrapper around the vector DB.

- `retrieval/hybrid_retriever.py`
  Combines BM25 and dense results into a single candidate set using a simple **fusion strategy** (e.g., Reciprocal Rank Fusion or weighted score fusion). Configurable parameters:
  - `k_bm25`, `k_dense` per query
  - fusion method & weights

### 3.2 Cross-encoder reranking

- `reranking/cross_encoder_reranker.py`
  Reranks the hybrid candidate list with a **cross-encoder** (Sentence-Transformers), scoring each `(query, passage)` pair and returning a small, high-precision set of passages.

---

## 4. LLM generation & grounding

### 4.1 Context packaging

- `generation/context_builder.py`
  Builds a compact, LLM-friendly context from top reranked passages, preserving:
  - source document
  - article numbers
  - chunk IDs

Example format:

```text
[SOURCE id=123, doc="Code du travail", article="L1233-3"]
…passage text…

[SOURCE id=124, doc="Code du travail", article="L1233-4"]
…passage text…
```

### 4.2 LLM orchestration

- `generation/llm_orchestrator.py`
  Calls an LLM (e.g., hosted or open-weight) with:
  - A **system prompt** enforcing:
    - “Use only the provided context”
    - “Answer in French”
    - “Cite sources using [SOURCE id=…]”
    - “Say you don’t know when context is insufficient”
  - Returns an answer and raw citation mentions.

---

## 5. Query pipeline & API

### 5.1 Query understanding

- `query/preprocess.py`
  Basic normalization while preserving legal tokens (article numbers, code names).

- `query/classify.py` (v1 = rule-based)
  Light classification of question type (e.g., direct citation vs conceptual) and hinting jurisdictions/domains.

- `query/build_structured_query.py`
  Produces:
  - `lexical_query` for BM25
  - `semantic_query` for embeddings
  - simple filters (jurisdiction, doc_type, dates)

### 5.2 FastAPI endpoint

- `app/main.py` exposes `/ask`:

```text
POST /ask
{
  "question": "Puis-je être licencié sans motif économique en tant que salarié au Maroc ?"
}
```

Pipeline:

1. Preprocess & classify the question.
2. Build structured query.
3. Call hybrid retriever (`k_bm25`, `k_dense`).
4. Rerank with cross-encoder.
5. Build context.
6. Call LLM for grounded answer.
7. Return answer + structured sources.

---

## 6. Evaluation

- `data/eval/eval_questions.jsonl`
  Small gold set of evaluation questions with expected sources.

- `eval/evaluate_retrieval.py`
  Computes retrieval metrics (e.g., recall@k, nDCG) against gold sources.

- `eval/evaluate_generation.py`
  Scaffold for manual/LLM-as-judge scoring of answer correctness, completeness, and citation accuracy.

- `eval/report_notebook.ipynb` (optional)
  Jupyter notebook for qualitative analysis (BM25 vs dense vs hybrid, typical failure modes).

---

## 7. How to run (v1)

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Prepare data**

```bash
python etl/ingest_legal_corpus.py
python etl/chunk_legal_docs.py
```

3. **Build indexes**

```bash
python indexing/index_bm25.py
python indexing/build_embeddings.py
python indexing/index_vectors.py
```

4. **Launch API**

```bash
uvicorn app.main:app --reload
```

Then query:

```bash
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" \
     -d '{"question": "Votre question ici"}'
```
