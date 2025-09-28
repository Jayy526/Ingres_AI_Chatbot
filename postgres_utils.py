import psycopg2


def run_sql_query(query: str, params=None):
    """Run a SQL query on Postgres and return results."""
    # Connect to Postgres
    conn = psycopg2.connect(
        host="localhost",  # or "postgres" if using Docker
        dbname="groundwater",
        user="postgres",
        password="postgres"
    )

    cur = conn.cursor()  # Create a cursor
    
    if params:
        cur.execute(query, params)  # Execute with parameters
    else:
        cur.execute(query)  # Execute the query
    
    # For INSERT/UPDATE/DELETE, commit the transaction
    if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
        conn.commit()
        rows = cur.rowcount  # Return number of affected rows
    else:
        rows = cur.fetchall()  # Fetch all results
    
    conn.close()  # Close connection
    return rows  # Return results
