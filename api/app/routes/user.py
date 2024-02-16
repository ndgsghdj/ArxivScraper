# Import necessary modules and classes from FastAPI and the app itself
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Import configurations and models from the app
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.users import Token, User, UserSignUp

# Import necessary functions from user handlers
from app.handlers.users import (
    authenticate_user, create_access_token, get_current_active_user,
    UserManager
)
from app.handlers.users import get_password_hash

# Create an instance of APIRouter to define routes related to user operations
user_router = APIRouter()

# Define a route for user signup
@user_router.post("/signup/")
async def signup(signup: UserSignUp):
    # Create a user manager instance
    user = UserManager()
    # Extract user data from signup form and create a User instance
    user_data = User(**signup.model_dump())
    # Hash the user's password before storing it
    user_data.__dict__.update({"password": get_password_hash(user_data.password)})
    # Attempt to create a new user
    u = user.create_user(user_data)
    # Check if the user creation was successful
    if u:
        # Return the signup data if successful
        return signup
    else:
        # Otherwise, raise an HTTPException indicating username already exists
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Define a route for user login to obtain an access token
@user_router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate the user based on the provided username and password
    user = authenticate_user(form_data.username, form_data.password)
    # Check if user authentication failed
    if not user:
        # Raise an HTTPException indicating incorrect email or password
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Define the expiration time for the access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Create an access token for the authenticated user
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    # Return the generated access token along with its type
    return {"access_token": access_token, "token_type": "bearer"}

# Define a route to retrieve information about the current user
@user_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    # Return the current user's information
    return current_user
