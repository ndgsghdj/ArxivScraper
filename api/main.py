import uvicorn
from fastapi import FastAPI, Depends

from app.routes.user import router
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

app.include_router(router, prefix="/api/user", tags=["users"])

if __name__ == "__main__":
    create_default_user()
    uvicorn.run(app)