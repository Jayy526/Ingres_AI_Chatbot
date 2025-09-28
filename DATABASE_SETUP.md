# PostgreSQL and PostGIS Database Setup

## Prerequisites

1. **Docker Desktop** must be installed and running
2. **PostgreSQL client tools** (optional, for direct database access)

## Quick Setup

### 1. Start the Database
```bash
# Start PostgreSQL with PostGIS
docker-compose up -d postgres

# Check if container is running
docker-compose ps
```

### 2. Verify Database Creation
```bash
# Connect to PostgreSQL
docker exec -it ingres_ai_chatbot-postgres-1 psql -U postgres -d groundwater

# In psql, run:
\dt  # List tables
SELECT PostGIS_Version();  # Check PostGIS
\q   # Exit
```

### 3. Test the Application
```bash
# Run the database test
python test_db.py

# Start the FastAPI server
python server.py

# Start the Streamlit UI (in another terminal)
streamlit run app.py
```

## Database Schema

### Tables Created:
- **groundwater_data**: Water level measurements with spatial data
- **wells**: Well information and locations
- **regions**: Administrative boundaries (for future use)

### Key Features:
- ✅ PostGIS spatial extensions enabled
- ✅ Spatial indexes for performance
- ✅ Sample data for 5 wells across different districts
- ✅ Time-series data for trend analysis
- ✅ Water quality parameters (pH, TDS)

## Sample Queries

### Get all wells with their latest measurements:
```sql
SELECT w.well_name, gd.water_level_meters, gd.measurement_date
FROM wells w
JOIN groundwater_data gd ON w.well_id = gd.well_id
WHERE gd.measurement_date = (
    SELECT MAX(measurement_date) 
    FROM groundwater_data gd2 
    WHERE gd2.well_id = gd.well_id
);
```

### Get spatial data for mapping:
```sql
SELECT well_id, ST_AsText(geom) as location, water_level_meters
FROM groundwater_data
WHERE measurement_date = '2023-03-15';
```

### Get trend data for charts:
```sql
SELECT measurement_date, AVG(water_level_meters) as avg_level
FROM groundwater_data
GROUP BY measurement_date
ORDER BY measurement_date;
```

## Troubleshooting

### If Docker isn't running:
1. Start Docker Desktop
2. Wait for it to fully load
3. Run `docker-compose up -d postgres`

### If database connection fails:
1. Check if container is running: `docker-compose ps`
2. Check logs: `docker-compose logs postgres`
3. Verify connection parameters in `postgres_utils.py`

### If PostGIS isn't available:
1. Check if the init script ran: `docker-compose logs postgres`
2. Manually run the init script if needed

## Alternative Setup (Without Docker)

If you prefer to install PostgreSQL locally:

1. Install PostgreSQL with PostGIS
2. Create the `groundwater` database
3. Run the SQL script from `init-db/01-init-databases.sql`
4. Update connection parameters in `postgres_utils.py`

