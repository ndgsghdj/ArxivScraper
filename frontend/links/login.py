import requests
from typing import Optional

class Authentication(requests.Session):
    def __init__(self, username: str, password: str, email: Optional[str]="") -> None:
        self.username = username
        self.password = password
        self.email = email
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
    
    def signup(self):
        url = "http://localhost:8000/api/user/signup"
        payload = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.post(url, json=payload, headers=headers)
        return response