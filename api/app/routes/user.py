from datetime import datetime, timedelta
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.users import Token, User, UserSignUp
from app.handlers.users import (
    authenticate_user, create_access_token, get_current_active_user,
    UserManager
)