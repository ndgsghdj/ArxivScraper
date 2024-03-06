import requests

class Papers(requests.Session):
    def __init__(self, token: str, url: str) -> None:
        self.token = token
        self.url = url
        super().__init__()
    
    def get_papers(self):
        url = "http://localhost:8000/api/papers/get-papers"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {"error": response.text}
    
    def scrape_paper(self):
        url = "http://localhost:8000/api/llm/scrape_paper/"
        headers = {
            "Content-Type": "application/json",
        }
        
        response = self.post(url, headers=headers, json={"url": self.url})
        return response.json() if response.status_code == 200 else {"error": response.text}
    
    def post_paper(self, data):
        url = "http://localhost:8000/api/papers/create-papers"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        response = self.post(url, headers=headers, json=data)
        return response.json() if response.status_code == 200 else {"error": response.text}
    
    def query_paper(self, query):
        url = "http://localhost:8000/api/llm/query/"
        headers = {
            "Content-Type": "application/json",
        }
        
        response = self.post(url, headers=headers, json={"query": query})
        return response.json() if response.status_code == 200 else {"error": response.text}
    
    def get_paper(self, paper_id):
        url = f"http://localhost:8000/api/papers/paper/{paper_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        result = self.get(url, headers=headers)
        return result.json() if result.status_code == 200 else {"error": result.text}