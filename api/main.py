import uvicorn
from fastapi import FastAPI, Depends

from app.routes import user, blog
from app.models.users import Profile, User
from src.handlers.users import get_password_hash, UserManager

app = FastAPI()

# Creating a default test user
def create_default_user():
    user_data = {
        "email": "nikola@gmail.com",
        "password": "redninja123",
    }

    user = User(**user_data)
    userManager = UserManager()
    userManager.create_user(user)

app.include_router(user.router, prefix="/api/user", tags=["users"])

if __name__ == "__main__":
    create_default_user()
    uvicorn.run(app)