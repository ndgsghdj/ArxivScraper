# Dependencies
There are two different sets of dependencies for the frontend and the api. It is recommended that you create two virtual environments for each directory.
To install the libraries and packages used for the frontend, run in your terminal:
```console
cd /path/to/api
pip3 install -r requirements.txt
```
To install the libraries and packages used for the backend, run in your terminal:
```console
cd /path/to/frontend
pip3 install -r requirements.txt
```

# Running the Frontend
Once you have installed the dependencies, assuming that your terminal console is in the frontend directory, you may run the frontend through:
```console
flet run main.py -w
```
This should open up a new window on your browser.

# Running the API
Once you have installed the dependencies, assuming that your terminal console is in the api directory, you may run the api through:
```console
python3 main.py
```
