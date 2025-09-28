import sqlite3


DB_PATH = "../data/bm25.db"


def bm25_search(query: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("SELECT content FROM docs WHERE docs MATCH ? LIMIT 3;", (query,))
        rows = [r[0] for r in cur.fetchall()]
    except Exception:
        rows = []
    conn.close()
    return rows


def insert_keywords(docs):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS docs USING fts5(content);")
    for d in docs:
        cur.execute("INSERT INTO docs(content) VALUES (?);", (d,))
    conn.commit()
    conn.close()