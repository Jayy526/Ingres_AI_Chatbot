from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from tools_minimal import run_rag_pipeline, process_uploaded_data


app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask_bot(query: Query):
    response = run_rag_pipeline(query.question)
    return {"answer": response}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Upload and process Excel/CSV files."""
    try:
        # Read file content
        file_content = await file.read()
        
        # Process the file
        result = process_uploaded_data(file_content, file.filename)
        
        if "error" in result:
            return {"error": result["error"]}, 400
        
        return result
        
    except Exception as e:
        return {"error": f"Upload failed: {str(e)}"}, 500


@app.get("/")
async def root():
    return {"message": "INGRES AI Chatbot API - Minimal SQLite Version", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "sqlite"}
