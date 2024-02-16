# Dependencies
It is recommended that you create a virtual environment for the dependencies in this project.

To install the libraries and packages used for the backend, run in your terminal:
```console
cd /path/to/api
pip3 install -r requirements.txt
```

# Running the API
In order to test the API on your own Firebase Firestore, ensure that you have JSON file of service account credentials generated from Google Cloud. The steps to do so are [here](https://firebase.google.com/docs/admin/setup#:~:text=To%20generate%20a,containing%20the%20key.). Place the JSON file with your service account credentials to the root directory of the project. Modify the `GOOGLE_APPLICATION_CREDENTIALS` variable in `.env.example` file with the file to your service account credentials JSON file.

Generate your H256 JWS key, and modify the `SECRET_KEY` variable in the `.env.example` file as well.

You must also ensure that you possess an OpenAI key to allow querying to an LLM model. Modify the `OPENAI_KEY` variable in `.env.example` file with your own OpenAI key. 

Lastly, rename the `.env.example` file to `.env`. 

Once you have installed the dependencies, assuming that your terminal console is in the api directory, you may run the api through:
```console
python3 main.py
```
