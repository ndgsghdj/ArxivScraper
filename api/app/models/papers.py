from pydantic import BaseModel
from datetime import datetime

class Paper(BaseModel):
    paper_id: int
    paper_url: str
    paper_name: str
    paper_description: str
    created_at: datetime = datetime.now()
    
    def __str__(self):
        return str(self.paper_name)
    
    def get_schema(self):
        print(self.model_json_schema(indent=2))
        return True