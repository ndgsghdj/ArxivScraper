import openai
import warnings
warnings.filterwarnings("ignore")
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

# get API Key
openai_api_key = os.getenv("../OPENAI_API_KEY")

# turn the llm response into a list to be used on UI side
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

# query llm method based on query_text
def query_llm(query_text):
    messages = [
        {"role": "system", "content": """In the following text, provide quotes ONLY FOUND IN THE TEXT containing physics phrases and keywords that are not commonly encountered in everyday conversation and text. For each quoted phrase, explain its meaning in laymen terms. If the explanation contains numerical numbers, use the words. For example, 1 should be one. 
    another example: if query_text = "The car going around in a circle experiences centripetal force, which is equals to the frictional force acting on the car"

    the output would be: 
    1. centripetal force:  a force that acts on a body moving in a circular path and is directed towards the centre around which the body is moving.
    2. frictional force: Friction is the force that resists motion when the surface of one object comes in contact with the surface of another."""
    },
        {"role": "user", "content": query_text},
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0 
    )
    listified_response = listify_llm_response(response.choices[0].message.content.strip())
    return listified_response


