# 💧 INGRES AI Chatbot

An intelligent groundwater analysis chatbot powered by AI, featuring PostgreSQL with PostGIS, vector search, and interactive data visualization.

## 🌟 Features

### 🤖 **AI-Powered Chat Interface**
- Natural language queries about groundwater data
- Intelligent response generation
- Context-aware conversations

### 📊 **Data Visualization**
- Interactive charts and graphs
- Trend analysis with matplotlib
- Real-time data visualization

### 📁 **File Upload Support**
- Excel (.xlsx, .xls) and CSV file uploads
- Automatic data validation and cleaning
- Smart column mapping
- Batch data processing

### 🗄️ **Advanced Database**
- PostgreSQL with PostGIS spatial extensions
- Spatial indexing for geographic queries
- Time-series data support
- Water quality parameter tracking

### 🔍 **Hybrid Search**
- Semantic search with Qdrant vector database
- BM25 keyword search with SQLite
- Intelligent query routing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ingres-ai-chatbot.git
   cd ingres-ai-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the database**
   ```bash
   docker-compose up -d postgres
   ```

4. **Run the application**
   ```bash
   # Terminal 1: Start the backend
   python server.py
   
   # Terminal 2: Start the frontend
   streamlit run app.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:8501`
   - Start chatting with the AI about groundwater data!

## 📋 Project Structure

```
ingres-ai-chatbot/
├── app.py                 # Streamlit frontend
├── server.py             # FastAPI backend
├── tools.py              # Core AI and data processing
├── postgres_utils.py     # Database utilities
├── qdrant_utils.py       # Vector search
├── sqlite_utils.py        # BM25 search
├── ingest.py             # Data ingestion
├── docker-compose.yml     # Docker services
├── requirements.txt      # Python dependencies
├── init-db/              # Database initialization
│   └── 01-init-databases.sql
├── static/               # Generated charts
├── sample_groundwater_data.csv
└── README.md
```

## 🎯 Usage

### 💬 **Chat Interface**
Ask natural language questions:
- *"Show me a trend of groundwater levels"*
- *"What are the water levels in each well?"*
- *"Generate a chart of the data"*
- *"Which wells have the highest water levels?"*

### 📊 **Data Upload**
1. Go to the "📊 Upload Data" tab
2. Select your Excel/CSV file
3. Preview the data
4. Click "💾 Upload to Database"

### 📈 **Data Analysis**
- **Trend Analysis**: Visualize water level changes over time
- **Spatial Analysis**: Map well locations and analyze geographic patterns
- **Quality Assessment**: Monitor pH, TDS, and other water quality parameters

## 🗄️ Database Schema

### Tables
- **`groundwater_data`**: Water level measurements with spatial data
- **`wells`**: Well information and locations
- **`regions`**: Administrative boundaries

### Key Features
- ✅ PostGIS spatial extensions
- ✅ Spatial indexes for performance
- ✅ Time-series data support
- ✅ Water quality tracking

## 🔧 Configuration

### Environment Variables
```bash
# Database
PG_URI=postgresql+psycopg://postgres:postgres@localhost:5432/groundwater

# Vector Database
QDRANT_URL=http://localhost:6333

# AI Model
OLLAMA_HOST=http://localhost:11434
```

### Docker Services
- **PostgreSQL + PostGIS**: Database with spatial extensions
- **Qdrant**: Vector database for semantic search
- **Ollama**: AI model server

## 📊 Sample Data

The application includes sample groundwater data:
- 5 wells across different districts
- 15 measurements with time-series data
- Water quality parameters (pH, TDS)
- Spatial coordinates for mapping

## 🛠️ Development

### Adding New Features
1. **Data Sources**: Add new data ingestion methods in `ingest.py`
2. **AI Capabilities**: Extend query processing in `tools.py`
3. **Visualizations**: Add new chart types in the chart generation functions
4. **Database**: Modify schema in `init-db/01-init-databases.sql`

### Testing
```bash
# Test database connection
python -c "from postgres_utils import run_sql_query; print('Database OK')"

# Test file upload
# Upload a CSV file through the web interface
```

## 📚 Documentation

- [Database Setup Guide](DATABASE_SETUP.md)
- [File Upload Guide](FILE_UPLOAD_GUIDE.md)
- [API Documentation](docs/api.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PostGIS** for spatial database capabilities
- **Qdrant** for vector search
- **Streamlit** for the web interface
- **FastAPI** for the backend API
- **Matplotlib** for data visualization

## 📞 Support

For questions and support:
- Create an issue on GitHub
- Check the documentation
- Review the sample data files

---

**🌊 Built for groundwater analysis and environmental monitoring**
