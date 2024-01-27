import uuid
import json
from datetime import datetime, time
from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import AnyUrl, HttpUrl
from pydantic.types import T, UUID4, constr
from pydantic.typing import NONE_TYPES

class User(BaseModel):
    username: Optional[str] = ""
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)
    created_at: Optional[datetime] = datetime.now()
    
    def __str__(self):
        return str(self.email)
    
    def get_schema(self):
        print(self.model_json_schema(indent=2))
        return True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserSignUp(BaseModel):
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)

class UserLogin(BaseModel):
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)