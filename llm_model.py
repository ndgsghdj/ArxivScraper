import openai
import warnings
warnings.filterwarnings("ignore")
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFium2Loader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
import chromadb
load_dotenv()

#get API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

#upload pdf files and embed them.

def embed():
    print("start")
    pdf_folder_path = "./papers/pdf/0704"
    documents = []
    for file in os.listdir(pdf_folder_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFium2Loader(pdf_path)
            documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(documents)
    client = chromadb.Client()
    if client.list_collections():
        consent_collection = client.create_collection("consent_collection")
    else:
        print("Collection already exists")
    vectordb = Chroma.from_documents(
        documents=chunked_documents,
        embedding=OpenAIEmbeddings()
    )
    print("end")
    return vectordb


vectordb = embed()

#llm = OpenAI(openai_api_key=openai_api_key)

