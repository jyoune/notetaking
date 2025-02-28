# notetaking

This repo contains several files related to a notetaker web service app:
* `notetaker.py` contains the NoteTaker object which stores and retrieves notes
* `api.py` is a FastAPI web service that functions as an interface for the notetaker
* `app.py` is a Flask frontend that makes requests to the FastAPI service
* `stream.py` is a Streamlit frontend that also makes requests to the FastAPI service

To run the app, navigate to the repo directory and type `uvicorn api:app` to start the FastAPI
service. From here you can make direct CLI requests to the FastAPI service to access the 
notetaker, but it is recommended to run either the Flask frontend with `Flask run` or the 
Streamlit frontend with `streamlit run stream.py`.