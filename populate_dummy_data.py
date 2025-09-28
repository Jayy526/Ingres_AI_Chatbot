#!/usr/bin/env python3
"""
Script to populate the database with dummy groundwater data.
This script will insert sample data into PostgreSQL and initialize the search databases.
"""

import pandas as pd
import time
from postgres_utils import run_sql_query
from qdrant_utils import initialize_qdrant
from sqlite_utils import initialize_sqlite

def wait_for_postgres():
    """Wait for PostgreSQL to be ready."""
    print("Waiting for PostgreSQL to be ready...")
    max_attempts = 30
    for attempt in range(max_attempts):
        try:
            # Try to connect to PostgreSQL
            result = run_sql_query("SELECT 1")
            print("✅ PostgreSQL is ready!")
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1}/{max_attempts}: PostgreSQL not ready yet...")
            time.sleep(2)
    
    print("❌ Could not connect to PostgreSQL after 30 attempts")
    return False

def populate_groundwater_data():
    """Populate the database with dummy groundwater data."""
    try:
        # Read the dummy data
        df = pd.read_csv('dummy_groundwater_data.csv')
        print(f"📊 Loaded {len(df)} rows of dummy data")
        
        # Insert data into PostgreSQL
        rows_inserted = 0
        errors = 0
        
        for _, row in df.iterrows():
            try:
                insert_query = """
                    INSERT INTO groundwater_data 
                    (well_id, location_name, latitude, longitude, depth_meters, 
                     water_level_meters, measurement_date, quality_ph, quality_tds, geom)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                """
                
                values = (
                    row['well_id'],
                    row['location_name'],
                    row['latitude'],
                    row['longitude'],
                    row['depth_meters'],
                    row['water_level_meters'],
                    row['measurement_date'],
                    row['quality_ph'],
                    row['quality_tds'],
                    row['longitude'],
                    row['latitude']
                )
                
                run_sql_query(insert_query, values)
                rows_inserted += 1
                
            except Exception as e:
                print(f"Error inserting row {row['well_id']}: {str(e)}")
                errors += 1
        
        print(f"✅ Inserted {rows_inserted} rows, {errors} errors")
        
        # Also insert into wells table for new wells
        unique_wells = df[['well_id', 'location_name', 'latitude', 'longitude', 'depth_meters']].drop_duplicates()
        
        for _, well in unique_wells.iterrows():
            try:
                # Check if well already exists
                check_query = "SELECT COUNT(*) FROM wells WHERE well_id = %s"
                count = run_sql_query(check_query, (well['well_id'],))[0][0]
                
                if count == 0:
                    insert_well_query = """
                        INSERT INTO wells (well_id, well_name, location_name, latitude, longitude, depth_meters, installation_date, geom)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                    """
                    
                    well_values = (
                        well['well_id'],
                        well['location_name'],  # Use location as well name
                        well['location_name'],
                        well['latitude'],
                        well['longitude'],
                        well['depth_meters'],
                        '2023-01-01',  # Default installation date
                        well['longitude'],
                        well['latitude']
                    )
                    
                    run_sql_query(insert_well_query, well_values)
                    print(f"✅ Added well {well['well_id']}")
                    
            except Exception as e:
                print(f"Error adding well {well['well_id']}: {str(e)}")
        
    except Exception as e:
        print(f"❌ Error populating data: {str(e)}")

def verify_data():
    """Verify that data was inserted correctly."""
    try:
        # Check groundwater_data table
        count_query = "SELECT COUNT(*) FROM groundwater_data"
        count = run_sql_query(count_query)[0][0]
        print(f"📊 Total groundwater measurements: {count}")
        
        # Check wells table
        wells_count = run_sql_query("SELECT COUNT(*) FROM wells")[0][0]
        print(f"🏭 Total wells: {wells_count}")
        
        # Show sample data
        sample_query = """
            SELECT well_id, location_name, water_level_meters, measurement_date, quality_ph
            FROM groundwater_data 
            ORDER BY measurement_date DESC 
            LIMIT 5
        """
        sample_data = run_sql_query(sample_query)
        print("\n📋 Sample data:")
        for row in sample_data:
            print(f"  {row[0]} | {row[1]} | {row[2]}m | {row[3]} | pH {row[4]}")
            
    except Exception as e:
        print(f"❌ Error verifying data: {str(e)}")

def main():
    """Main function to set up dummy database."""
    print("🚀 Setting up dummy groundwater database...")
    
    # Wait for PostgreSQL
    if not wait_for_postgres():
        return
    
    # Initialize search databases
    print("\n🔍 Initializing search databases...")
    initialize_qdrant()
    initialize_sqlite()
    
    # Populate with dummy data
    print("\n📊 Populating database with dummy data...")
    populate_groundwater_data()
    
    # Verify data
    print("\n✅ Verifying data...")
    verify_data()
    
    print("\n🎉 Dummy database setup complete!")
    print("\nYou can now run:")
    print("  - Backend API: python server.py")
    print("  - Frontend UI: streamlit run app.py")
    print("  - Or use Docker: docker-compose up")

if __name__ == "__main__":
    main()
