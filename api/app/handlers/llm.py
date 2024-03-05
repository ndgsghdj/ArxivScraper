# Importing necessary modules
import openai
import warnings
import os
from dotenv import load_dotenv, find_dotenv

# Importing modules from langchain package
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFium2Loader
from langchain.document_loaders import DirectoryLoader

# Importing modules from langchain.prompts package
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Ignoring warnings
warnings.filterwarnings("ignore")

# Loading environment variables
load_dotenv()

# Getting API Key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to truncate text into chunks of a certain size
def truncate_text(text, chunk_size):
    ans = []
    counter = 0
    curr = ""
    i = 0
    while i < len(text):
        curr += text[i]
        counter += 1
        if counter == chunk_size:
            while i < len(text) and (text[i].isalpha() or text[i].isnumeric() or text[i] == "-" or text[i] == "_"):
                curr += text[i]
                i += 1
            ans.append(curr)
            curr = ""
            counter = 0
        i += 1
    if curr != "":
        ans.append(curr)
    return ans



# Function to query the OpenAI LLM based on query_text
def query_llm(query_text):
    messages = [
        {"role": "system", "content": """In the following text, provide quotes ONLY FOUND IN THE TEXT containing physics phrases and keywords that are not commonly encountered in everyday conversation and text. For each quoted phrase, explain its meaning. If the explanation contains numerical numbers, use the words. For example, 1 should be one. 
    another example: if query_text = "The car going around in a circle experiences centripetal force, which is equals to the frictional force acting on the car"

    the output would be: 
    1. centripetal force:  a force that acts on a body moving in a circular path and is directed towards the centre around which the body is moving.
    2. frictional force: Friction is the force that resists motion when the surface of one object comes in contact with the surface of another."""},
        {"role": "user", "content": query_text},
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0 
    )
    listified_response = listify_llm_response(response.choices[0].message.content.strip())
    return listified_response



"""1. centripetal force:  a force that acts on a body moving in a circular path and is directed towards the centre around which the body is moving.
    2. frictional force: Friction is the force that resists motion when the surface of one object comes in contact with the surface of another."""
#
# -> ["centripetal force:  a force that acts on a body moving in a circular path and is directed towards the centre around which the body is moving.", 
# "frictional force: Friction is the force that resists motion when the surface of one object comes in contact with the surface of another."]

# Function to turn the OpenAI LLM response into a list to be used on the UI side
def listify_llm_response(response):
    ans = []
    curr = ""
    for i in range(len(response)):
        if 3 < i < len(response) - 1 and response[i].isnumeric() and response[i+1]==".":
            ans.append(curr)
            curr = ""
        if response[i] != "\n":
            curr += response[i]
    ans.append(curr)
    return ans
