from flet import ft, response
from pydantic import BaseModel
import fitz  # PyMuPDF
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

PDF_FILE = "sample.pdf"

class Query(BaseModel):
    query_text: str

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

def query_llm(query_text):
    messages = [
        {"role": "system", "content": """In the following text, provide quotes ONLY FOUND IN THE TEXT containing physics phrases and keywords that are not commonly encountered in everyday conversation and text. For each quoted phrase, explain its meaning. If the explanation contains numerical numbers, use the words. For example, 1 should be one. 
    another example: if query_text = "The car going around in a circle experiences centripetal force, which is equals to the frictional force acting on the car"

    the output would be: 
    1. centripetal force:  a force that acts on a body moving in a circular path and is directed towards the centre around which the body is moving.
    2. frictional force: Friction is the force that resists motion when the surface of one object comes in contact with the surface of another."""
        },
        {"role": "user", "content": query_text},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0 
    )
    listified_response = listify_llm_response(response.choices[0].message.content.strip())
    return listified_response

@ft.GET("/")
def pdf_viewer():
    with open("index.html", "r") as f:
        html_content = f.read()
    return response.HTML(html_content)

@ft.POST("/query/")
def query_and_highlight(query: Query):
    llm_response = query_llm(query.query_text)

    pdf_document = fitz.open(PDF_FILE)

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        for highlight_text in llm_response:
            for match in page.search_for(highlight_text):
                page.add_highlight_annot(match)

    # you know just saving it and stuff 
    pdf_document.save("highlighted_pdf.pdf", incremental=True)
    pdf_document.close()

    return response.FileResponse("highlighted_pdf.pdf")

ft.app(target=__name__)
