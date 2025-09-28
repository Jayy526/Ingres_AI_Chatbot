import sqlite3
import os

DB_PATH = "groundwater_dummy.db"

def run_sql_query(query: str, params=None):
    """Run a SQL query on SQLite and return results."""
    if not os.path.exists(DB_PATH):
        raise Exception(f"Database file {DB_PATH} not found. Please run simple_setup.py first.")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        # For INSERT/UPDATE/DELETE, commit the transaction
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            conn.commit()
            rows = cursor.rowcount
        else:
            rows = cursor.fetchall()
        
        return rows
        
    finally:
        conn.close()
