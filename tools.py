from db.postgres_utils import run_sql_query
from db.qdrant_utils import semantic_search
from db.sqlite_utils import bm25_search


def run_rag_pipeline(question: str) -> str:
    """Decide retrieval route based on query type."""


    if "map" in question.lower():
        return "[Map tool placeholder: would call PostGIS and return visualization URL]"
    elif "trend" in question.lower():
        return "[Timeseries tool placeholder: would call Postgres + matplotlib chart]"
    else:
        # Try hybrid search
        semantic_results = semantic_search(question)
        keyword_results = bm25_search(question)

        # Return top result safely
        if semantic_results:
            return semantic_results[0]
        elif keyword_results:
            return keyword_results[0]
        else:
            return "No results found."
