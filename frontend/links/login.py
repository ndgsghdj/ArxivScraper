import requests

class Login(requests.Session):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        super().__init__()
    
    def login(self):
        url = "http://localhost:8000/api/user/token"
        payload = {
            "username": self.username,
            "password": self.password
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = self.post(url, data=payload, headers=headers)
        return response