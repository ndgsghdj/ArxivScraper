from app.config import db
from app.models.users import User, TokenData
from users import UserManager as u

class PaperManager:
    def __init__(self):
        self.db = db
        self.coll = "papers"
    
    def get_user_papers(self, username):
        docs = self.db.collection("users").where("username", "==", username).collection(self.coll).stream()
        papers_list = [doc.to_dict() for doc in docs]
        return papers_list
    
    def create_new_paper(self, username, paper):
        doc = self.db.collection("users").where("username", "==", username).collection(self.coll).document(str(paper.paper_id)).set(paper.dict())
        if not doc:
            raise("document not saved")
        # Add the new document to the database
        return True
    
    def delete_paper(self, username, paper_id):
        doc = self.db.collection("users").where("username", "==", username).collection(self.coll).document(paper_id).delete()
        return True
    
    def get_paper(self, username, paper_id):
        doc = self.db.collection("users").where("username", "==", username).collection(self.coll).document(paper_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
            
def get_papers(username: str):
    p = PaperManager()
    papers = p.get_user_papers(username)
    return papers

def create_paper(username: str, paper):
    p = PaperManager()
    papers = p.create_new_paper(username, paper)
    return papers

def delete_paper(username: str, paper_id: str):
    p = PaperManager()
    papers = p.delete_paper(username, paper_id)
    return papers