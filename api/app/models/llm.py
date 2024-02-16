# Importing necessary modules and classes
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Defining a Pydantic BaseModel subclass for the response structure
class LLMResponse(BaseModel):
    # Declaring a field 'keywords' which is a list of strings
    keywords: List[str]
    # Declaring a field 'created_at' which defaults to the current datetime
    created_at: datetime = datetime.now()

# Defining another Pydantic BaseModel subclass for the query structure
class Query(BaseModel):
    # Declaring a field 'query' which is a string
    query: str
