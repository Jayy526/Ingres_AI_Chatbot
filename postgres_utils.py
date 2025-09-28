import psycopg2


def run_sql_query(query: str):
    """Run a SQL query on Postgres and return results."""
    # Connect to Postgres
    conn = psycopg2.connect(
        host="localhost",  # or "postgres" if using Docker
        dbname="groundwater",
        user="ingres",
        password="ingres"
    )

    cur = conn.cursor()  # Create a cursor
    cur.execute(query)  # Execute the query
    rows = cur.fetchall()  # Fetch all results
    conn.close()  # Close connection
    return rows  # Return results
