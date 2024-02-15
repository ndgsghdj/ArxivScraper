from pydantic import BaseModel, HttpUrl, validator
from datetime import datetime

class ArxivURL(BaseModel):
    url: str

    @classmethod
    def validate_url(cls, url):
        if "arxiv.org/html/" not in str(url):
            raise ValueError("Invalid arXiv html URL. It should contain 'arxiv.org/html/'")
        return url

    @validator("url", pre=True)
    def prepend_http(cls, v):
        if isinstance(v, str) and not v.startswith(("http://", "https://")):
            return "http://" + v
        return v

    @validator("url")
    def validate_arxiv_url(cls, v):
        if isinstance(v, str) and not v.startswith("http://arxiv.org/html/") and not v.startswith("https://arxiv.org/html/"):
            raise ValueError("Invalid arXiv URL. It should start with 'http://arxiv.org/html/' or 'https://arxiv.org/html/'")
        return v

class Paper(BaseModel):
    paper_id: int
    paper_url: ArxivURL
    paper_name: str
    paper_description: str
    created_at: datetime = datetime.now()
    
    def __str__(self):
        return str(self.paper_name)
    
    def get_schema(self):
        print(self.model_json_schema(indent=2))
        return True