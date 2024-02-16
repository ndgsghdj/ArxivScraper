# Importing necessary modules and classes from the app
from app.config import db
from app.models.users import User, TokenData
from app.handlers.users import UserManager as u
from app.models.papers import Paper

# Defining a class to manage papers
class PaperManager:
    def __init__(self):
        # Initializing the PaperManager with the database instance and collection name
        self.db = db
        self.coll = "papers"
    
    # Method to get papers associated with a user
    def get_user_papers(self, username):
        try:
            # Attempting to fetch documents from the collection
            docs = self.db.collection("users").document(username).collection(self.coll).stream()
        except:
            # Returning False if an error occurs
            return False
        # Converting documents to a list of dictionaries
        papers_list = [doc.to_dict() for doc in docs]
        return papers_list
    
    # Method to create a new paper for a user
    def create_new_paper(self, username, paper: Paper):
        # Setting the paper document in the collection
        doc = self.db.collection("users").document(username).collection(self.coll).document(str(paper.paper_id)).set(paper.model_dump())
        # Checking if the document was saved successfully
        if not doc:
            raise("document not saved")
        # Returning True if document saved
        return True
    
    # Method to delete a paper for a user
    def delete_paper(self, username, paper_id):
        # Deleting the paper document from the collection
        doc = self.db.collection("users").document(username).collection(self.coll).document(paper_id).delete()
        # Checking if the document was deleted successfully
        if not doc:
            raise("document not deleted")
        # Returning True if document deleted
        return True
    
    # Method to get a specific paper for a user
    def get_paper(self, username, paper_id):
        # Fetching the paper document from the collection
        doc = self.db.collection("users").document(username).collection(self.coll).document(paper_id).get()
        # Checking if the document exists
        if doc.exists:
            return doc.to_dict()  # Returning the paper document as a dictionary
        else:
            return None  # Returning None if document not found
            
# Function to get papers associated with a user
def get_papers(username: str):
    p = PaperManager()
    papers = p.get_user_papers(username)
    return papers

# Function to create a new paper for a user
def create_paper(username: str, paper):
    p = PaperManager()
    papers = p.create_new_paper(username, paper)
    return papers

# Function to delete a paper for a user
def delete_paper(username: str, paper_id: str):
    p = PaperManager()
    papers = p.delete_paper(username, paper_id)
    return papers

# Function to get a specific paper for a user
def get_paper(username: str, paper_id: str):
    p = PaperManager()
    papers = p.get_paper(username, paper_id)
    return papers
