from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
import openai

app = FastAPI()

# Serve static files 
app.mount("/static", StaticFiles(directory="static"), name="static")

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Upload endpoint to accept PDF file uploads
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# PDF viewer endpoint 
@app.get("/pdf/{filename}")
async def get_pdf(filename: str):
    pdf_path = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(pdf_path)

# Default endpoint to serve frontend stuff
@app.get("/")
def read_root():
    return FileResponse("static/index.html")
