from fastapi import FastAPI, File, UploadFile
import openai

app = FastAPI()

# Initialize OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

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
        {"role": "system", "content": "System prompt here"},
        {"role": "user", "content": query_text},
    ]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    listified_response = listify_llm_response(response.choices[0].message.content.strip())
    return listified_response

# PDF upload stuff
@app.post('/upload-pdf/')
def upload_pdf(pdf: UploadFile = File(...)):
    with open(pdf.filename, "wb") as file:
        file.write(pdf.file.read())
    
    response = query_llm("Generate comments for the PDF")
    return {"pdf_url": pdf.filename, "comments": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
