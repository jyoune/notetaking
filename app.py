from flask import Flask, render_template, request, redirect, url_for
import requests
import json



app = Flask(__name__)

# GET CONSTANTS FROM FASTAPI SCRIPT AND BASEMODEL ITEM (Note)
from api import URL_CONST, PORT_CONST, Note
FASTAPI_URL = "http://" + URL_CONST + ":" + str(PORT_CONST)


@app.route("/", methods=['GET', 'POST'])
def root():
    response = requests.get(f"{FASTAPI_URL}/list")
    # notes is list of note NAMES, not NOTE OBJECTS!!!
    notes = response.json()["notes"]
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_note':
            note_name = request.form.get('note_name')
            note_text = request.form.get('note_text')
            new_note = {'name': note_name, 'text': note_text}
            response = requests.post(f"{FASTAPI_URL}/add", json=new_note)
            return redirect("/")
        elif action == 'search_term':
            term = request.form.get('term')
            return redirect(url_for("search_term", term=term))
    return render_template('home.html', names=notes)


@app.route("/search")
def search_term():
    term = request.args.get('term')
    response = requests.get(f"{FASTAPI_URL}/find?term={term}")
    notes = response.json()["results"]
    return render_template('search.html', term=term, names=notes)


@app.route("/note")
def display_note():
    note_name = request.args.get('note_name')
    response = requests.get(f"{FASTAPI_URL}/note/{note_name}")
    if response.status_code == 200:
        note = response.json()
        return render_template('display_note.html', note=note)
    else:
        return "Not found", 404


@app.route("/add")
def add_note(name: str, text: str):
    # get these from the HTML form on the homepage!!!
    note = {"name": name, "text": text}
    response = requests.post(f"{FASTAPI_URL}/add", note)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

