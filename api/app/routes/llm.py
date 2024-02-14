from fastapi import APIRouter
from app.models.llm import ArxivURL

llm_router = APIRouter()

@llm_router.post("/scrape_paper/")
def scrape_paper_html(url: ArxivURL):
    url.validate_url(url.url)
    return {"url": url.url}