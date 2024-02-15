from fastapi import APIRouter, UploadFile, File
from app.models.papers import ArxivURL
from app.models.llm import Query
from app.handlers.llm import query_llm
from urllib.request import urlopen
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
from dotenv import load_dotenv

llm_router = APIRouter()

# Directory to store uploaded files
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Post endpoint to accept URL input
@llm_router.post("/scrape_paper/")
async def scrape_paper_html(url: ArxivURL):
    url.prepend_http(url.url)
    url.validate_url(url.url)
    paper = urlopen(url.url, timeout=10)
    html_bytes = paper.read()
    html = html_bytes.decode("utf-8")
    return {"html": html}

@llm_router.post("/query/")
async def query_llm_endpoint(query: Query):
    response = query_llm(query.query)
    return {"response": response}

# Upload endpoint to accept PDF file uploads
@llm_router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# PDF viewer endpoint 
@llm_router.get("/pdf/{filename}")
async def get_pdf(filename: str):
    pdf_path = os.path.join(UPLOAD_DIR, filename)
    return FileResponse(pdf_path)

# Default endpoint to serve frontend stuff
@llm_router.get("/")
def read_root():
    return FileResponse("static/index.html")