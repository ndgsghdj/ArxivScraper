from pydantic import BaseModel, HttpUrl, validator

class ArxivURL(BaseModel):
    url: HttpUrl

    @classmethod
    def validate_url(cls, url):
        if "arxiv.org/html/" not in url:
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
