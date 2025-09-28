# 📁 Excel/CSV File Upload Guide

## 🚀 **How to Add Excel/CSV Files to Your Chatbot**

Your INGRES AI Chatbot now supports uploading Excel (.xlsx, .xls) and CSV files containing groundwater data!

### 📋 **Supported File Formats**
- ✅ **CSV files** (.csv)
- ✅ **Excel files** (.xlsx, .xls)
- ✅ **Automatic format detection**

### 🎯 **How to Use**

1. **Start the application:**
   ```bash
   # Terminal 1: Start the backend
   python server.py
   
   # Terminal 2: Start the frontend
   streamlit run app.py
   ```

2. **Open the Upload Tab:**
   - Go to the "📊 Upload Data" tab in the Streamlit interface
   - Click "Choose a file" to select your Excel/CSV file
   - Preview your data before uploading
   - Click "💾 Upload to Database" to process the file

### 📊 **Expected Data Format**

Your file should contain columns like:

| Column | Description | Example | Required |
|--------|-------------|---------|----------|
| `well_id` | Unique well identifier | W001, W002 | ✅ Yes |
| `location_name` | Well location name | Downtown, North District | ❌ No |
| `latitude` | Latitude coordinate | 28.6139 | ❌ No |
| `longitude` | Longitude coordinate | 77.2090 | ❌ No |
| `water_level_meters` | Water level in meters | 12.3 | ✅ Yes |
| `measurement_date` | Date of measurement | 2023-01-15 | ✅ Yes |
| `quality_ph` | pH value | 7.2 | ❌ No |
| `quality_tds` | TDS in mg/L | 450.5 | ❌ No |
| `depth_meters` | Well depth | 45.5 | ❌ No |

### 🔧 **Smart Column Mapping**

The system automatically recognizes common column name variations:

- **well_id**: `well_id`, `wellid`, `well`, `id`
- **location_name**: `location_name`, `location`, `site`, `site_name`
- **latitude**: `latitude`, `lat`, `y`
- **longitude**: `longitude`, `lon`, `lng`, `x`
- **water_level_meters**: `water_level_meters`, `water_level`, `level`, `depth`
- **measurement_date**: `measurement_date`, `date`, `timestamp`
- **quality_ph**: `quality_ph`, `ph`, `ph_value`
- **quality_tds**: `quality_tds`, `tds`, `tds_value`

### 🧹 **Data Cleaning Features**

✅ **Automatic data cleaning:**
- Removes empty rows
- Validates coordinates (latitude: -90 to 90, longitude: -180 to 180)
- Filters out invalid water levels (must be > 0)
- Converts data types automatically
- Handles missing values intelligently

✅ **Data validation:**
- Checks required columns
- Validates coordinate ranges
- Ensures positive water levels
- Converts dates automatically

### 📈 **Sample Data Files**

I've created sample files for testing:

1. **`sample_groundwater_data.csv`** - CSV format with 10 records
2. **`sample_groundwater_data.xlsx`** - Excel format (create with: `python create_sample_excel.py`)

### 🔄 **Complete Workflow**

1. **Upload File** → System reads and validates
2. **Data Preview** → Shows first 10 rows and column info
3. **Data Cleaning** → Removes invalid rows, standardizes format
4. **Database Insert** → Stores in PostgreSQL with PostGIS
5. **Success Confirmation** → Shows rows processed and any errors

### 🗄️ **Database Integration**

Uploaded data is stored in the `groundwater_data` table with:
- ✅ **Spatial data** (PostGIS geometry)
- ✅ **Time-series data** for trend analysis
- ✅ **Water quality parameters**
- ✅ **Automatic indexing** for performance

### 🎨 **After Upload**

Once uploaded, you can:
- **Ask questions**: "Show me trends from the new data"
- **Generate charts**: "Create a chart of water levels"
- **Query data**: "What are the latest measurements?"
- **Spatial analysis**: "Show me wells on a map"

### 🚨 **Error Handling**

The system handles common issues:
- ❌ **Invalid file formats** → Clear error messages
- ❌ **Missing required columns** → Lists what's needed
- ❌ **Invalid data** → Shows which rows had errors
- ❌ **Database connection issues** → Graceful fallback

### 💡 **Tips for Best Results**

1. **Use consistent column names** across files
2. **Include coordinates** for spatial analysis
3. **Use standard date formats** (YYYY-MM-DD)
4. **Check data quality** before uploading
5. **Start with small files** to test the process

### 🔧 **Technical Details**

- **Backend**: FastAPI with file upload endpoint
- **Frontend**: Streamlit with file uploader widget
- **Database**: PostgreSQL with PostGIS extensions
- **Processing**: Pandas for data manipulation
- **Validation**: Custom data cleaning functions

### 🎯 **Next Steps**

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Start the database**: `docker-compose up -d postgres`
3. **Run the application**: `python server.py` + `streamlit run app.py`
4. **Upload your data**: Use the "📊 Upload Data" tab
5. **Start analyzing**: Ask questions about your data!

---

**🎉 Your chatbot is now ready to handle Excel/CSV groundwater data uploads!**

