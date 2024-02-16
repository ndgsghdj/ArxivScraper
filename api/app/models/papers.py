# Importing necessary modules and classes
from pydantic import BaseModel, HttpUrl, validator
from datetime import datetime
from uuid import uuid4

# Defining a Pydantic BaseModel subclass for ArxivURL
class ArxivURL(BaseModel):
    # Declaring a field 'url' which is a string
    url: str

    # Class method to validate the URL format
    @classmethod
    def validate_url(cls, url):
        # Check if the URL contains "arxiv.org/html/"
        if "arxiv.org/html/" not in str(url):
            # If not, raise a ValueError
            raise ValueError("Invalid arXiv html URL. It should contain 'arxiv.org/html/'")
        return url

    # Validator to prepend "http://" to the URL if missing
    @validator("url", pre=True)
    def prepend_http(cls, v):
        # Check if the input is a string and doesn't start with "http://" or "https://"
        if isinstance(v, str) and not v.startswith(("http://", "https://")):
            # Prepend "http://" to the URL
            return "http://" + v
        return v

    # Validator to ensure the URL starts with "http://arxiv.org/html/" or "https://arxiv.org/html/"
    @validator("url")
    def validate_arxiv_url(cls, v):
        # Check if the input is a string and starts with a valid prefix
        if isinstance(v, str) and not v.startswith("http://arxiv.org/html/") and not v.startswith("https://arxiv.org/html/"):
            # If not, raise a ValueError
            raise ValueError("Invalid arXiv URL. It should start with 'http://arxiv.org/html/' or 'https://arxiv.org/html/'")
        return v

# Defining a Pydantic BaseModel subclass for Paper
class Paper(BaseModel):
    # Declaring a field 'paper_id' which defaults to a new UUID string
    paper_id: str = str(uuid4())
    # Declaring a field 'paper_url' which is an instance of ArxivURL
    paper_url: ArxivURL
    # Declaring a field 'paper_name' which is a string
    paper_name: str
    # Declaring a field 'paper_html' which defaults to an empty string
    paper_html: str = ""
    # Declaring a field 'paper_keywords' which is a string
    paper_keywords: str
    # Declaring a field 'created_at' which defaults to the current datetime
    created_at: datetime = datetime.now()

    # Method to return a string representation of the paper
    def __str__(self):
        return str(self.paper_name)

    # Method to get the JSON schema of the model
    def get_schema(self):
        # Print the JSON schema with indentation
        print(self.model_json_schema(indent=2))
        return True
