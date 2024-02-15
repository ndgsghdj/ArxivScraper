from pydantic import BaseModel
from typing import List
from datetime import datetime

class LLMResponse(BaseModel):
    keywords: List[str]
    created_at: datetime = datetime.now()

class Query(BaseModel):
    query: str