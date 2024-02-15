import uvicorn
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from app.routes.user import user_router
from app.routes.llm import llm_router
from app.routes.papers import papers_router

from app.models.users import User
from app.handlers.users import get_password_hash, UserManager

app = FastAPI()

# Creating a default test user for dev, not used in prod
def create_default_user():
    user_data = {
        "username": "nikola",
        "email": "nikola@gmail.com",
        "password": "redninja123",
    }

    user = User(**user_data)
    userManager = UserManager()
    userManager.create_user(user)

app.include_router(user_router, prefix="/api/user", tags=["users"])
app.include_router(llm_router, prefix="/api/llm", tags=["papers"])
app.include_router(papers_router, prefix="/api/papers", tags=["papers"])
# Serve static files 
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    create_default_user()
    uvicorn.run(app)