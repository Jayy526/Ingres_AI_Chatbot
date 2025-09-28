#!/usr/bin/env python3
"""
Simple setup script that creates a SQLite-based dummy database
without requiring Docker or PostgreSQL.
"""

import sqlite3
import pandas as pd
import os
from pathlib import Path

def create_sqlite_database():
    """Create a SQLite database with groundwater data."""
    db_path = "groundwater_dummy.db"
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create groundwater_data table
    cursor.execute('''
        CREATE TABLE groundwater_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            well_id VARCHAR(50) NOT NULL,
            location_name VARCHAR(100),
            latitude DECIMAL(10, 8),
            longitude DECIMAL(11, 8),
            depth_meters DECIMAL(8, 2),
            water_level_meters DECIMAL(8, 2),
            measurement_date DATE,
            quality_ph DECIMAL(4, 2),
            quality_tds DECIMAL(8, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create wells table
    cursor.execute('''
        CREATE TABLE wells (
            well_id VARCHAR(50) PRIMARY KEY,
            well_name VARCHAR(100) NOT NULL,
            location_name VARCHAR(100),
            latitude DECIMAL(10, 8),
            longitude DECIMAL(11, 8),
            depth_meters DECIMAL(8, 2),
            installation_date DATE,
            status VARCHAR(20) DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create regions table
    cursor.execute('''
        CREATE TABLE regions (
            region_id INTEGER PRIMARY KEY AUTOINCREMENT,
            region_name VARCHAR(100) NOT NULL,
            region_type VARCHAR(50),
            population INTEGER,
            area_sqkm DECIMAL(10, 2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("✅ Created SQLite database structure")
    return conn

def populate_sample_data(conn):
    """Populate the database with sample data."""
    cursor = conn.cursor()
    
    # Insert sample wells
    wells_data = [
        ('W001', 'Central Well', 'Downtown Area', 28.6139, 77.2090, 45.5, '2020-01-15'),
        ('W002', 'North Well', 'North District', 28.7041, 77.1025, 52.3, '2020-03-20'),
        ('W003', 'South Well', 'South District', 28.5355, 77.3910, 38.7, '2020-05-10'),
        ('W004', 'East Well', 'East District', 28.6129, 77.2295, 41.2, '2020-07-15'),
        ('W005', 'West Well', 'West District', 28.6149, 77.1885, 48.9, '2020-09-20'),
        ('W006', 'Industrial Well', 'Industrial Area', 28.6500, 77.2500, 55.0, '2020-11-01'),
        ('W007', 'Residential Well', 'Residential Zone', 28.5800, 77.3200, 42.3, '2021-01-10'),
        ('W008', 'Commercial Well', 'Commercial District', 28.6200, 77.1800, 48.7, '2021-03-15'),
        ('W009', 'Suburban Well', 'Suburban Area', 28.7000, 77.1500, 38.9, '2021-05-20'),
        ('W010', 'Rural Well', 'Rural Zone', 28.5500, 77.4000, 62.1, '2021-07-25')
    ]
    
    cursor.executemany('''
        INSERT INTO wells (well_id, well_name, location_name, latitude, longitude, depth_meters, installation_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', wells_data)
    
    # Insert sample groundwater measurements
    measurements_data = [
        # W001 measurements
        ('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 12.3, '2023-01-15', 7.2, 450.5),
        ('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 11.8, '2023-02-15', 7.1, 465.2),
        ('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 11.5, '2023-03-15', 7.3, 442.8),
        ('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 11.2, '2023-04-15', 7.0, 458.1),
        ('W001', 'Downtown Area', 28.6139, 77.2090, 45.5, 10.9, '2023-05-15', 7.2, 445.7),
        
        # W002 measurements
        ('W002', 'North District', 28.7041, 77.1025, 52.3, 15.2, '2023-01-15', 6.9, 520.1),
        ('W002', 'North District', 28.7041, 77.1025, 52.3, 14.8, '2023-02-15', 7.0, 535.7),
        ('W002', 'North District', 28.7041, 77.1025, 52.3, 14.5, '2023-03-15', 7.2, 518.3),
        ('W002', 'North District', 28.7041, 77.1025, 52.3, 14.1, '2023-04-15', 6.8, 542.9),
        ('W002', 'North District', 28.7041, 77.1025, 52.3, 13.8, '2023-05-15', 7.1, 525.4),
        
        # W003 measurements
        ('W003', 'South District', 28.5355, 77.3910, 38.7, 8.9, '2023-01-15', 7.5, 380.2),
        ('W003', 'South District', 28.5355, 77.3910, 38.7, 8.6, '2023-02-15', 7.4, 395.8),
        ('W003', 'South District', 28.5355, 77.3910, 38.7, 8.3, '2023-03-15', 7.6, 372.1),
        ('W003', 'South District', 28.5355, 77.3910, 38.7, 8.0, '2023-04-15', 7.3, 388.5),
        ('W003', 'South District', 28.5355, 77.3910, 38.7, 7.7, '2023-05-15', 7.5, 375.2),
        
        # W004 measurements
        ('W004', 'East District', 28.6129, 77.2295, 41.2, 9.8, '2023-01-15', 7.0, 420.5),
        ('W004', 'East District', 28.6129, 77.2295, 41.2, 9.5, '2023-02-15', 6.9, 435.2),
        ('W004', 'East District', 28.6129, 77.2295, 41.2, 9.2, '2023-03-15', 7.1, 418.7),
        ('W004', 'East District', 28.6129, 77.2295, 41.2, 8.9, '2023-04-15', 6.8, 442.3),
        ('W004', 'East District', 28.6129, 77.2295, 41.2, 8.6, '2023-05-15', 7.0, 425.9),
        
        # W005 measurements
        ('W005', 'West District', 28.6149, 77.1885, 48.9, 13.7, '2023-01-15', 7.3, 485.3),
        ('W005', 'West District', 28.6149, 77.1885, 48.9, 13.4, '2023-02-15', 7.2, 500.1),
        ('W005', 'West District', 28.6149, 77.1885, 48.9, 13.1, '2023-03-15', 7.4, 482.6),
        ('W005', 'West District', 28.6149, 77.1885, 48.9, 12.8, '2023-04-15', 7.1, 495.8),
        ('W005', 'West District', 28.6149, 77.1885, 48.9, 12.5, '2023-05-15', 7.3, 478.4),
        
        # Additional wells from dummy data
        ('W006', 'Industrial Area', 28.6500, 77.2500, 55.0, 18.5, '2023-04-15', 6.8, 580.2),
        ('W006', 'Industrial Area', 28.6500, 77.2500, 55.0, 18.2, '2023-05-15', 6.9, 585.1),
        ('W007', 'Residential Zone', 28.5800, 77.3200, 42.3, 14.2, '2023-04-15', 7.1, 420.8),
        ('W007', 'Residential Zone', 28.5800, 77.3200, 42.3, 13.9, '2023-05-15', 7.2, 425.3),
        ('W008', 'Commercial District', 28.6200, 77.1800, 48.7, 16.8, '2023-04-15', 7.0, 510.5),
        ('W008', 'Commercial District', 28.6200, 77.1800, 48.7, 16.5, '2023-05-15', 7.1, 515.8),
        ('W009', 'Suburban Area', 28.7000, 77.1500, 38.9, 12.1, '2023-04-15', 7.3, 380.9),
        ('W009', 'Suburban Area', 28.7000, 77.1500, 38.9, 11.8, '2023-05-15', 7.4, 385.2),
        ('W010', 'Rural Zone', 28.5500, 77.4000, 62.1, 22.3, '2023-04-15', 6.9, 650.7),
        ('W010', 'Rural Zone', 28.5500, 77.4000, 62.1, 22.0, '2023-05-15', 7.0, 655.4)
    ]
    
    cursor.executemany('''
        INSERT INTO groundwater_data (well_id, location_name, latitude, longitude, depth_meters, 
                                   water_level_meters, measurement_date, quality_ph, quality_tds)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', measurements_data)
    
    # Insert sample regions
    regions_data = [
        ('Downtown', 'Urban', 50000, 15.5),
        ('North District', 'Suburban', 30000, 25.2),
        ('South District', 'Suburban', 25000, 20.8),
        ('East District', 'Urban', 40000, 18.3),
        ('West District', 'Urban', 35000, 16.7),
        ('Industrial Area', 'Industrial', 15000, 12.4),
        ('Residential Zone', 'Residential', 45000, 22.1),
        ('Commercial District', 'Commercial', 20000, 8.9),
        ('Suburban Area', 'Suburban', 28000, 19.6),
        ('Rural Zone', 'Rural', 10000, 45.2)
    ]
    
    cursor.executemany('''
        INSERT INTO regions (region_name, region_type, population, area_sqkm)
        VALUES (?, ?, ?, ?)
    ''', regions_data)
    
    conn.commit()
    print("✅ Populated database with sample data")
    
    # Show statistics
    cursor.execute("SELECT COUNT(*) FROM groundwater_data")
    measurements_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM wells")
    wells_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM regions")
    regions_count = cursor.fetchone()[0]
    
    print(f"📊 Database Statistics:")
    print(f"   - Groundwater measurements: {measurements_count}")
    print(f"   - Wells: {wells_count}")
    print(f"   - Regions: {regions_count}")
    
    return conn

def create_sqlite_postgres_utils():
    """Create a SQLite version of postgres_utils.py"""
    sqlite_utils_content = '''import sqlite3
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
'''
    
    with open('sqlite_postgres_utils.py', 'w') as f:
        f.write(sqlite_utils_content)
    
    print("✅ Created SQLite version of postgres_utils.py")

def main():
    """Main setup function."""
    print("🚀 Setting up SQLite dummy database...")
    print("=" * 50)
    
    # Create database
    conn = create_sqlite_database()
    
    # Populate with sample data
    populate_sample_data(conn)
    
    # Create SQLite version of postgres_utils
    create_sqlite_postgres_utils()
    
    # Create static directory
    Path("static").mkdir(exist_ok=True)
    
    conn.close()
    
    print("\n🎉 SQLite dummy database setup complete!")
    print("\nTo use this database, you need to:")
    print("1. Replace 'from postgres_utils import run_sql_query' with 'from sqlite_postgres_utils import run_sql_query'")
    print("2. Or modify your code to use SQLite instead of PostgreSQL")
    print("\nDatabase file: groundwater_dummy.db")
    print("You can now run your application!")

if __name__ == "__main__":
    main()
