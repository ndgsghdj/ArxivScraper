from datetime import datetime, time
from typing import Optional, Annotated
from pydantic import BaseModel
from pydantic.networks import AnyUrl, HttpUrl
from pydantic.types import UUID4, constr

class User(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=100)
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)
    is_active: Optional[bool] = True
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
    username: Optional[str] = None

class UserSignUp(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=255)
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)

class UserLogin(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=255)
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    password: constr(min_length=8, max_length=255)