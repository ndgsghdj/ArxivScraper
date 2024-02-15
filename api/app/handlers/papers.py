from app.config import db
from app.models.users import User, TokenData
from app.handlers.users import UserManager as u
from app.models.papers import Paper

class PaperManager:
    def __init__(self):
        self.db = db
        self.coll = "papers"
    
    def get_user_papers(self, username):
        try:
            docs = self.db.collection("users").document(username).collection(self.coll).stream()
        except:
            return False
        papers_list = [doc.to_dict() for doc in docs]
        return papers_list
    
    def create_new_paper(self, username, paper: Paper):
        doc = self.db.collection("users").document(username).collection(self.coll).document(str(paper.paper_id)).set(paper.model_dump())
        if not doc:
            raise("document not saved")
        # Add the new document to the database
        return True
    
    def delete_paper(self, username, paper_id):
        doc = self.db.collection("users").document(username).collection(self.coll).document(paper_id).delete()
        if not doc:
            raise("document not deleted")
        return True
    
    def get_paper(self, username, paper_id):
        doc = self.db.collection("users").document(username).collection(self.coll).document(paper_id).get()
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

def get_paper(username: str, paper_id: str):
    p = PaperManager()
    papers = p.get_paper(username, paper_id)
    return papers