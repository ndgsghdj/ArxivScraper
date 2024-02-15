from fastapi import APIRouter, Depends, HTTPException
from app.handlers.papers import get_papers, create_paper, delete_paper, get_paper
from app.models.papers import Paper
from app.models.users import User
from app.handlers.users import get_current_active_user

papers_router = APIRouter()

@papers_router.get("/get-papers")
async def getPapers(currentUser: User = Depends(get_current_active_user)):
    return get_papers(currentUser.username)

@papers_router.post("/create-papers")
async def create_new_paper(paper: Paper, currentUser: User = Depends(get_current_active_user)):
   created_paper = create_paper(currentUser.username, paper)
   if created_paper:
         return {"message": "Paper created successfully"}
   else:
         raise(
                HTTPException(
                    status_code=400,
                    detail="Paper not created",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            ) 

@papers_router.get("/paper/{id}")
async def GetPaper(id: str, currentUser: User = Depends(get_current_active_user)):
    paper = get_paper(currentUser.username, id)
    if not paper is None:
        return paper
    else:
        raise(
                HTTPException(
                    status_code=404,
                    detail="Paper not found",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            )             
            
@papers_router.delete("/remove-paper/{id}", response_model=dict)
def remove_paper(id:str, currentUser: User = Depends(get_current_active_user)):
    deleted_paper = delete_paper(currentUser.username, id)
    if deleted_paper:
        return {"message": "Paper deleted successfully"}
    else:
        raise(
                HTTPException(
                    status_code=400,
                    detail="Paper not deleted",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            )