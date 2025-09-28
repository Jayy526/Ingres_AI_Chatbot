from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import numpy as np
import json

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Collection name for groundwater data
COLLECTION_NAME = "groundwater_docs"

def initialize_qdrant():
    """Initialize Qdrant collection for groundwater documents."""
    try:
        # Create collection if it doesn't exist
        collections = client.get_collections()
        collection_names = [col.name for col in collections.collections]
        
        if COLLECTION_NAME not in collection_names:
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )
            print(f"Created collection: {COLLECTION_NAME}")
        else:
            print(f"Collection {COLLECTION_NAME} already exists")
            
        # Add sample documents
        add_sample_documents()
        
    except Exception as e:
        print(f"Error initializing Qdrant: {str(e)}")

def add_sample_documents():
    """Add sample groundwater documents to Qdrant."""
    sample_docs = [
        {
            "id": 1,
            "text": "Groundwater levels in the downtown area have been declining over the past year. The average water level is 12.3 meters with pH levels around 7.2.",
            "metadata": {"location": "downtown", "well_id": "W001", "date": "2023-01-15"}
        },
        {
            "id": 2,
            "text": "North district wells show higher water levels at 15.2 meters. Water quality is good with TDS levels around 520 mg/L.",
            "metadata": {"location": "north", "well_id": "W002", "date": "2023-01-15"}
        },
        {
            "id": 3,
            "text": "South district has the shallowest water table at 8.9 meters. The water quality is excellent with pH 7.5 and low TDS.",
            "metadata": {"location": "south", "well_id": "W003", "date": "2023-01-15"}
        },
        {
            "id": 4,
            "text": "Industrial area wells show contamination concerns with elevated TDS levels above 580 mg/L. Immediate attention required.",
            "metadata": {"location": "industrial", "well_id": "W006", "date": "2023-04-15"}
        },
        {
            "id": 5,
            "text": "Residential zone water quality is within acceptable limits. Regular monitoring shows stable pH levels around 7.1.",
            "metadata": {"location": "residential", "well_id": "W007", "date": "2023-04-15"}
        }
    ]
    
    try:
        # Generate random vectors for demonstration (in real app, use proper embeddings)
        points = []
        for doc in sample_docs:
            # Generate random 384-dimensional vector
            vector = np.random.random(384).tolist()
            
            point = PointStruct(
                id=doc["id"],
                vector=vector,
                payload={
                    "text": doc["text"],
                    "metadata": doc["metadata"]
                }
            )
            points.append(point)
        
        # Upsert points to collection
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )
        print(f"Added {len(sample_docs)} sample documents to Qdrant")
        
    except Exception as e:
        print(f"Error adding sample documents: {str(e)}")

def semantic_search(query: str, limit: int = 3) -> list:
    """Perform semantic search on groundwater documents."""
    try:
        # Generate random query vector (in real app, use proper embedding model)
        query_vector = np.random.random(384).tolist()
        
        # Search in Qdrant
        search_results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit
        )
        
        # Extract text from results
        results = []
        for result in search_results:
            if result.payload and "text" in result.payload:
                results.append(result.payload["text"])
        
        return results
        
    except Exception as e:
        print(f"Error in semantic search: {str(e)}")
        return ["Groundwater data shows normal levels across all monitoring wells."]

# Initialize Qdrant on import
initialize_qdrant()