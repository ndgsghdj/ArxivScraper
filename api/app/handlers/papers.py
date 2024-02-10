from app.config import db, SECRET_KEY, ALGORITHM
from app.models.users import User, TokenData
from users import UserManager as u

class PaperManager:
    def __init__(self, db, coll):
        self.db = db
        self.coll = "papers"
    
    def get_user_papers(self, model):
        docs = db.collection("users").where("username", "==", model.username).collection(self.coll).stream()
        papers_list = [doc.to_dict() for doc in docs]
        return papers_list