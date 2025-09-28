# INGRES AI Chatbot - Dummy Database Setup

This guide will help you set up a dummy database to run the INGRES AI Chatbot application without requiring Docker or PostgreSQL.

## 🚀 Quick Start

### Option 1: Simple SQLite Setup (Recommended)

1. **Run the setup script:**
   ```bash
   python simple_setup.py
   ```

2. **Test the setup:**
   ```bash
   python test_minimal.py
   ```

3. **Start the application:**
   ```bash
   # Backend API
   python server_minimal.py
   
   # Frontend UI (in another terminal)
   streamlit run app.py
   ```

### Option 2: Full Docker Setup

1. **Start Docker services:**
   ```bash
   docker-compose up -d postgres qdrant
   ```

2. **Populate database:**
   ```bash
   python populate_dummy_data.py
   ```

3. **Start the application:**
   ```bash
   # Backend API
   python server.py
   
   # Frontend UI (in another terminal)
   streamlit run app.py
   ```

## 📊 Database Contents

The dummy database includes:

- **35 groundwater measurements** across 10 different wells
- **10 wells** with location data and installation dates
- **10 regions** with population and area information
- **Sample data** covering 5 months (Jan-May 2023)

### Sample Wells:
- W001: Central Well (Downtown Area)
- W002: North Well (North District)
- W003: South Well (South District)
- W004: East Well (East District)
- W005: West Well (West District)
- W006: Industrial Well (Industrial Area)
- W007: Residential Well (Residential Zone)
- W008: Commercial Well (Commercial District)
- W009: Suburban Well (Suburban Area)
- W010: Rural Well (Rural Zone)

## 🔧 Available Scripts

### Setup Scripts:
- `simple_setup.py` - Creates SQLite database with dummy data
- `populate_dummy_data.py` - Populates PostgreSQL database (requires Docker)
- `start_app.py` - Full Docker setup script

### Test Scripts:
- `test_minimal.py` - Tests SQLite setup
- `test_simple.py` - Tests with minimal dependencies
- `test_setup.py` - Tests full setup

### Server Scripts:
- `server_minimal.py` - SQLite-based API server
- `server_simple.py` - SQLite-based API with basic features
- `server.py` - Full PostgreSQL-based API server

## 📁 Database Files

- `groundwater_dummy.db` - SQLite database file
- `groundwater_search.db` - SQLite search database
- `static/` - Directory for generated charts and static files

## 🧪 Testing the Setup

Run the test script to verify everything is working:

```bash
python test_minimal.py
```

Expected output:
```
🧪 Testing INGRES AI Chatbot Setup
==================================================
🔍 Testing database connection...
✅ Groundwater measurements: 35
✅ Wells: 10
✅ Sample data:
   W001 | Downtown Area | 10.9m | 2023-05-15
   W002 | North District | 13.8m | 2023-05-15
   W003 | South District | 7.7m | 2023-05-15

🤖 Testing RAG pipeline...
✅ Q: What are the groundwater levels in downtown?
   A: Groundwater levels in downtown area average 12.3 meters with pH 7.2...
✅ Q: Show me a trend chart
   A: 📊 Groundwater Data Chart...
✅ Q: What is the water quality like?
   A: Residential zone maintains stable pH 7.1 with good water quality...

📊 Testing data upload...
✅ Upload successful: Successfully processed test_data.csv
   Rows processed: 0
   Errors: 2

🎉 All tests completed!
```

## 🌐 Accessing the Application

Once running, you can access:

- **Frontend UI**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🔍 Sample Queries

Try these sample questions in the chatbot:

1. "What are the groundwater levels in downtown?"
2. "Show me a trend chart"
3. "What is the water quality like?"
4. "How many wells are there?"
5. "What are the average water levels?"

## 📊 Data Upload

You can upload CSV or Excel files with groundwater data. The system expects columns like:

- `well_id` - Well identifier
- `location_name` - Location name
- `latitude` - Latitude coordinate
- `longitude` - Longitude coordinate
- `water_level_meters` - Water level in meters
- `measurement_date` - Date of measurement
- `quality_ph` - pH level
- `quality_tds` - Total Dissolved Solids

## 🛠️ Troubleshooting

### Common Issues:

1. **Module not found errors**: Install missing dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database connection errors**: Ensure the database file exists:
   ```bash
   python simple_setup.py
   ```

3. **Port already in use**: Change ports in the server configuration

4. **Docker issues**: Use the SQLite setup instead:
   ```bash
   python simple_setup.py
   python test_minimal.py
   python server_minimal.py
   ```

## 📝 Notes

- The SQLite setup is recommended for development and testing
- The Docker setup provides the full production environment
- All dummy data is realistic and follows groundwater monitoring standards
- The system supports both text-based and chart-based responses
- File upload functionality works with CSV and Excel files

## 🎯 Next Steps

1. Test the application with the provided dummy data
2. Upload your own groundwater data files
3. Customize the chatbot responses
4. Deploy to production using Docker

For more information, see the main README.md file.
