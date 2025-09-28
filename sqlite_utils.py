import sqlite3
import re
from typing import List

# SQLite database file
DB_FILE = "groundwater_search.db"

def initialize_sqlite():
    """Initialize SQLite database for BM25 search."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create documents table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY,
                text TEXT NOT NULL,
                metadata TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create FTS5 virtual table for full-text search
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
                text,
                metadata,
                content='documents',
                content_rowid='id'
            )
        ''')
        
        # Insert sample documents
        add_sample_documents()
        
        conn.commit()
        conn.close()
        print("SQLite database initialized successfully")
        
    except Exception as e:
        print(f"Error initializing SQLite: {str(e)}")

def add_sample_documents():
    """Add sample groundwater documents to SQLite."""
    sample_docs = [
        "Groundwater levels in downtown area average 12.3 meters with pH 7.2",
        "North district wells show 15.2 meter water levels and 520 mg/L TDS",
        "South district has shallow water table at 8.9 meters with excellent quality",
        "Industrial area shows contamination with TDS above 580 mg/L",
        "Residential zone maintains stable pH 7.1 with good water quality",
        "Commercial district wells at 16.8 meters depth with 510 mg/L TDS",
        "Suburban area shows 12.1 meter levels with 380 mg/L TDS",
        "Rural zone has deepest wells at 22.3 meters with 650 mg/L TDS"
    ]
    
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Check if documents already exist
        cursor.execute("SELECT COUNT(*) FROM documents")
        count = cursor.fetchone()[0]
        
        if count == 0:
            for i, doc in enumerate(sample_docs, 1):
                cursor.execute('''
                    INSERT INTO documents (id, text, metadata) 
                    VALUES (?, ?, ?)
                ''', (i, doc, f'{{"source": "sample", "id": {i}}}'))
            
            # Update FTS index
            cursor.execute("INSERT INTO documents_fts(documents_fts) VALUES('rebuild')")
            
            conn.commit()
            print(f"Added {len(sample_docs)} sample documents to SQLite")
        
        conn.close()
        
    except Exception as e:
        print(f"Error adding sample documents: {str(e)}")

def bm25_search(query: str, limit: int = 3) -> List[str]:
    """Perform BM25 search on groundwater documents."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Clean and prepare query
        clean_query = re.sub(r'[^\w\s]', ' ', query.lower())
        search_terms = clean_query.split()
        
        if not search_terms:
            return []
        
        # Build FTS query
        fts_query = ' OR '.join([f'"{term}"' for term in search_terms])
        
        # Search using FTS5
        cursor.execute('''
            SELECT text, bm25(documents_fts) as rank
            FROM documents_fts 
            WHERE documents_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        ''', (fts_query, limit))
        
        results = cursor.fetchall()
        conn.close()
        
        # Return just the text content
        return [result[0] for result in results]
        
    except Exception as e:
        print(f"Error in BM25 search: {str(e)}")
        return ["Groundwater monitoring shows normal levels across all districts."]

# Initialize SQLite on import
initialize_sqlite()