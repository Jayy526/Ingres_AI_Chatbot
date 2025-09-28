#!/usr/bin/env python3
"""
Minimal test script to verify the dummy database setup is working correctly.
"""

import sqlite3
from sqlite_postgres_utils import run_sql_query
from tools_minimal import run_rag_pipeline, process_uploaded_data
import pandas as pd

def test_database_connection():
    """Test database connection and basic queries."""
    print("🔍 Testing database connection...")
    
    try:
        # Test basic connection
        result = run_sql_query("SELECT COUNT(*) FROM groundwater_data")
        measurements_count = result[0][0]
        print(f"✅ Groundwater measurements: {measurements_count}")
        
        # Test wells table
        result = run_sql_query("SELECT COUNT(*) FROM wells")
        wells_count = result[0][0]
        print(f"✅ Wells: {wells_count}")
        
        # Test sample query
        result = run_sql_query("""
            SELECT well_id, location_name, water_level_meters, measurement_date 
            FROM groundwater_data 
            ORDER BY measurement_date DESC 
            LIMIT 3
        """)
        print("✅ Sample data:")
        for row in result:
            print(f"   {row[0]} | {row[1]} | {row[2]}m | {row[3]}")
        
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

def test_rag_pipeline():
    """Test the RAG pipeline."""
    print("\n🤖 Testing RAG pipeline...")
    
    test_questions = [
        "What are the groundwater levels in downtown?",
        "Show me a trend chart",
        "What is the water quality like?"
    ]
    
    for question in test_questions:
        try:
            response = run_rag_pipeline(question)
            print(f"✅ Q: {question}")
            print(f"   A: {response[:100]}...")
        except Exception as e:
            print(f"❌ RAG pipeline failed for '{question}': {str(e)}")

def test_data_upload():
    """Test data upload functionality."""
    print("\n📊 Testing data upload...")
    
    try:
        # Create a small test CSV
        test_data = {
            'well_id': ['TEST001', 'TEST002'],
            'location_name': ['Test Location 1', 'Test Location 2'],
            'latitude': [28.6, 28.7],
            'longitude': [77.2, 77.3],
            'water_level_meters': [10.5, 12.3],
            'measurement_date': ['2023-12-01', '2023-12-01'],
            'quality_ph': [7.0, 7.2],
            'quality_tds': [400.0, 450.0]
        }
        
        df = pd.DataFrame(test_data)
        csv_content = df.to_csv(index=False).encode('utf-8')
        
        # Test upload
        result = process_uploaded_data(csv_content, "test_data.csv")
        
        if "error" in result:
            print(f"❌ Upload failed: {result['error']}")
        else:
            print(f"✅ Upload successful: {result['message']}")
            print(f"   Rows processed: {result['rows_processed']}")
            print(f"   Errors: {result['errors']}")
        
    except Exception as e:
        print(f"❌ Upload test failed: {str(e)}")

def main():
    """Run all tests."""
    print("🧪 Testing INGRES AI Chatbot Setup")
    print("=" * 50)
    
    # Test database
    db_ok = test_database_connection()
    
    if db_ok:
        # Test RAG pipeline
        test_rag_pipeline()
        
        # Test data upload
        test_data_upload()
        
        print("\n🎉 All tests completed!")
        print("\nYour dummy database is ready to use!")
        print("\nTo start the application:")
        print("1. Backend API: python server_minimal.py")
        print("2. Frontend UI: streamlit run app.py")
        print("3. Or use: uvicorn server_minimal:app --reload")
    else:
        print("\n❌ Setup failed. Please check the database creation.")

if __name__ == "__main__":
    main()
