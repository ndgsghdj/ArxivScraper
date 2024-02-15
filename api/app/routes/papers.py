from fastapi import APIRouter

papers_router = APIRouter()

@papers_router.get("/")
def read_papers():
    return {"papers": "papers"}