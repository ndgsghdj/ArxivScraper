import requests

class Papers(requests.Session):
    def __init__(self, token: str) -> None:
        self.token = token
        super().__init__()
    
    def get_papers(self):
        url = "http://localhost:8000/api/llm/"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {"error": response.text}