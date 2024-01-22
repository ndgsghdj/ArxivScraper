import openai
import warnings
warnings.filterwarnings("ignore")
import os
from dotenv import load_dotenv, find_dotenv

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFium2Loader
from langchain.document_loaders import DirectoryLoader

load_dotenv()

#get API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key,model_name='gpt-3.5-turbo-instruct')

#upload pdf files and embed them.

def embed():
    loader = DirectoryLoader('./test_folders', glob="./*.pdf", loader_cls=PyPDFium2Loader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    persist_directory="./vector_db"
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

    vectordb = Chroma.from_documents(documents=texts,   
        embedding=embedding,
        persist_directory=persist_directory
    )
    vectordb.persist()
    vectordb = None
    vectordb = Chroma(persist_directory=persist_directory, 
    embedding_function=embedding
    )
    return vectordb

vectordb = embed()
retriever = vectordb.as_retriever()
docs = retriever.get_relevant_documents("How much money did Pando raise?")
retriever = vectordb.as_retriever(search_kwargs={"k": 2})
qa_chain = RetrievalQA.from_chain_type(llm=llm, 
                                  chain_type="stuff", 
                                  retriever=retriever, 
                                  return_source_documents=True)

query = "what is a phonon mediated decay of an atom"
llm_response = qa_chain(query)
print(llm_response['result'])