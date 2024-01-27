from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from api.config import db, SECRET_KEY, ALGORITHM
from app.models.users import User, TokenData

class UserManager:
    def __init__(self):
        self.db = db
        self.collection = "users"

    def create_user(self, model):
        doc = db.collection(self.collection).document(str(model.email)).get()