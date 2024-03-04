import requests

class Papers(requests.Session):
    def __init__(self, token: str, url: str) -> None:
        self.token = token
        self.url = url
        super().__init__()
    
    def get_papers(self):
        url = "http://localhost:8000/api/llm/"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {"error": response.text}
    
    def get_paper(self):
        url = "http://localhost:8000/api/llm/scrape_paper/"
        headers = {
            "Content-Type": "application/json",
        }
        
        response = self.post(url, headers=headers,json={"url": self.url})
        return response.json() if response.status_code == 200 else {"error": response.text}

p = Papers(token="", url="https://arxiv.org/html/2402.05137v1")
with open("index.html", "w") as f:
    f.write(p.get_paper()["html"])