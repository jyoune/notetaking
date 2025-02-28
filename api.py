from fastapi import FastAPI
from notetaker import NoteTaker
from pydantic import BaseModel
import uvicorn

nt = NoteTaker()
app = FastAPI()

# CONSTANTS FOR URL/PORT
URL_CONST = "127.0.0.1"
PORT_CONST = 8000

class Note(BaseModel):
    name: str
    text: str


@app.get("/")
async def root():
    return {"message": "API for notetaking. Resources available for GET requests: /list/ returns a list of all notes. /find?term=x returns a list of every note containing the term x. /note/x returns the full text of the note with the name x. POST to /add with a dictionary or file to add a note to the notetaker."}


@app.get("/list")
async def list_notes():
    return {"notes" : nt.get_notes()}


@app.get("/find")
async def find_term(term: str):
    return {"term": term, "results" : nt.find(term)}


@app.get("/note/{note_name}")
async def get_note(note_name: str):
    return nt[note_name]


@app.post("/add")
async def add_note(note: Note):
    note_dict = note.dict()
    nt.add(note_dict["name"], note_dict["text"])
    return {"message": f"successfully added note {note_dict["name"]}"}


if __name__ == "__main__":
    uvicorn.run("api:api", host=URL_CONST, port=PORT_CONST, reload=False)