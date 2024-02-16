import requests
import json
from typing import Optional

class Authenticator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Authenticator, cls).__new__(cls)
            cls._instance.is_authenticated = False
        return cls._instance
    
    def is_logged_in(self):
        return self.is_authenticated
    
    def change_authentication_state(self, state: bool):
        self.is_authenticated = state

auth = Authenticator()

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
        if response.status_code == 200:
            token_data = response.json()
            self.auth = (token_data["access"], token_data["bearer"])
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