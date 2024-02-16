# Import necessary modules and classes from FastAPI and the app itself
from fastapi import APIRouter, Depends, HTTPException

# Import functions related to paper operations from the app handlers
from app.handlers.papers import get_papers, create_paper, delete_paper, get_paper

# Import the Paper model from the app
from app.models.papers import Paper

# Import the User model and the get_current_active_user function from the user handlers
from app.models.users import User
from app.handlers.users import get_current_active_user

# Create an instance of APIRouter to define routes related to paper operations
papers_router = APIRouter()

# Define a route to get papers for the current user
@papers_router.get("/get-papers")
async def getPapers(currentUser: User = Depends(get_current_active_user)):
    return get_papers(currentUser.username)

# Define a route to create a new paper for the current user
@papers_router.post("/create-papers")
async def create_new_paper(paper: Paper, currentUser: User = Depends(get_current_active_user)):
    # Attempt to create a new paper
    created_paper = create_paper(currentUser.username, paper)
    # Check if the paper creation was successful
    if created_paper:
        # Return success message if paper was created successfully
        return {"message": "Paper created successfully"}
    else:
        # Raise an HTTPException if paper creation failed
        raise HTTPException(
            status_code=400,
            detail="Paper not created",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Define a route to get a specific paper by its ID for the current user
@papers_router.get("/paper/{id}")
async def GetPaper(id: str, currentUser: User = Depends(get_current_active_user)):
    # Attempt to retrieve the paper with the specified ID
    paper = get_paper(currentUser.username, id)
    # Check if the paper was found
    if paper is not None:
        # Return the paper if found
        return paper
    else:
        # Raise an HTTPException if the paper was not found
        raise HTTPException(
            status_code=404,
            detail="Paper not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Define a route to delete a specific paper by its ID for the current user
@papers_router.delete("/remove-paper/{id}", response_model=dict)
def remove_paper(id:str, currentUser: User = Depends(get_current_active_user)):
    # Attempt to delete the paper with the specified ID
    deleted_paper = delete_paper(currentUser.username, id)
    # Check if the paper deletion was successful
    if deleted_paper:
        # Return success message if paper was deleted successfully
        return {"message": "Paper deleted successfully"}
    else:
        # Raise an HTTPException if paper deletion failed
        raise HTTPException(
            status_code=400,
            detail="Paper not deleted",
            headers={"WWW-Authenticate": "Bearer"},
        )
