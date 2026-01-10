import os

structure = """
legal-rag-v1/
├─ README.md
├─ requirements.txt
├─ pyproject.toml
├─ .env.example
├─ docker-compose.yml
├─ data/
│  ├─ raw/
│  │  └─ README.md
│  ├─ processed/
│  │  ├─ documents.parquet
│  │  └─ chunks.parquet
│  └─ eval/
│     └─ eval_questions.jsonl
├─ etl/
│  ├─ ingest_corpus.py
│  ├─ chunk_docs.py
│  └─ build_metadata.py
├─ indexing/
│  ├─ index_bm25.py
│  ├─ build_embeddings.py
│  └─ index_vectors.py
├─ retrieval/
│  ├─ bm25_retriever.py
│  ├─ dense_retriever.py
│  └─ hybrid_retriever.py
├─ reranking/
│  └─ cross_encoder_reranker.py
├─ generation/
│  ├─ context_builder.py
│  └─ llm_orchestrator.py
├─ query/
│  ├─ preprocess.py
│  ├─ classify.py
│  └─ build_structured_query.py
├─ app/
│  ├─ main.py
│  └─ config.py
├─ eval/
│  ├─ evaluate_retrieval.py
│  ├─ evaluate_generation.py
│  └─ evaluation_report_notebook.ipynb
└─ scripts/
   ├─ run_pipeline_cli.py
   └─ demo_notebook.ipynb
"""

def create_structure(base_path, struct_text):
    path_stack = [base_path]

    for line in struct_text.strip().splitlines():
        # Clean the line to get just the name
        clean_line = line.replace('├─', '').replace('└─', '').replace('│', '').strip()
        if not clean_line: continue

        # Determine depth based on indentation (every 3 spaces is a level)
        indent = line.find(' ') if ' ' in line else 0
        depth = (line.count('│') + line.count('├') + line.count('└'))

        # Adjust stack to current depth
        while len(path_stack) > depth + 1:
            path_stack.pop()

        target_path = os.path.join(path_stack[-1], clean_line)

        if clean_line.endswith('/'):
            os.makedirs(target_path, exist_ok=True)
            path_stack.append(target_path)
        elif '.' in clean_line: # It's a file
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, 'a'): os.utime(target_path, None)
        else: # Folder without trailing slash
            os.makedirs(target_path, exist_ok=True)
            path_stack.append(target_path)

if __name__ == "__main__":
    create_structure(".", structure)
    print("Legal RAG v1 structure created successfully.")
