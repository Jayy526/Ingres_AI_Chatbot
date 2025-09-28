from db.qdrant_utils import insert_embeddings
from db.sqlite_utils import insert_keywords
import os


DATA_DIR = "../data/docs"


def ingest_docs():
    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith('.txt'):
            with open(os.path.join(DATA_DIR, file), 'r', encoding='utf-8') as f:
                docs.append(f.read())


    insert_embeddings(docs)
    insert_keywords(docs)
    print(f"Ingested {len(docs)} docs into Qdrant + SQLite")


if __name__ == "__main__":
    ingest_docs()