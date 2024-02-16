# Importing necessary modules and classes
from datetime import datetime, time
from typing import Optional, Annotated

# Importing BaseModel from Pydantic for model creation
from pydantic import BaseModel

# Importing specific types from Pydantic for field validation
from pydantic.networks import AnyUrl, HttpUrl
from pydantic.types import UUID4, constr

# Defining a Pydantic BaseModel subclass for User
class User(BaseModel):
    # Declaring a field 'username' which is a constrained string
    username: constr(strip_whitespace=True, min_length=1, max_length=100)
    # Declaring a field 'email' which is a constrained string
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    # Declaring a field 'password' which is a constrained string
    password: constr(min_length=8, max_length=255)
    # Declaring an optional field 'is_active' which defaults to True
    is_active: Optional[bool] = True
    # Declaring an optional field 'created_at' which defaults to the current datetime
    created_at: Optional[datetime] = datetime.now()

    # Method to return a string representation of the user
    def __str__(self):
        return str(self.email)

    # Method to get the JSON schema of the model
    def get_schema(self):
        # Print the JSON schema with indentation
        print(self.model_json_schema(indent=2))
        return True

# Defining a Pydantic BaseModel subclass for Token
class Token(BaseModel):
    # Declaring a field 'access_token' which is a string
    access_token: str
    # Declaring a field 'token_type' which is a string
    token_type: str

# Defining a Pydantic BaseModel subclass for TokenData
class TokenData(BaseModel):
    # Declaring an optional field 'username' which defaults to None
    username: Optional[str] = None

# Defining a Pydantic BaseModel subclass for UserSignUp
class UserSignUp(BaseModel):
    # Declaring a field 'username' which is a constrained string
    username: constr(strip_whitespace=True, min_length=1, max_length=255)
    # Declaring a field 'email' which is a constrained string
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    # Declaring a field 'password' which is a constrained string
    password: constr(min_length=8, max_length=255)

# Defining a Pydantic BaseModel subclass for UserLogin
class UserLogin(BaseModel):
    # Declaring a field 'username' which is a constrained string
    username: constr(strip_whitespace=True, min_length=1, max_length=255)
    # Declaring a field 'email' which is a constrained string
    email: constr(strip_whitespace=True, min_length=1, max_length=100)
    # Declaring a field 'password' which is a constrained string
    password: constr(min_length=8, max_length=255)
