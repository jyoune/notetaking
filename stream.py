import streamlit as st
import requests
import time

from api import URL_CONST, PORT_CONST
FASTAPI_URL = "http://" + URL_CONST + ":" + str(PORT_CONST)


def list_notes() -> list[str]:
    response = requests.get(f"{FASTAPI_URL}/list")
    notes = response.json()["notes"]
    return notes


def get_note(note_name:str) -> dict[str:str] | None:
    response = requests.get(f"{FASTAPI_URL}/note/{note_name}")
    if response.status_code == 200:
        return response.json()


def add_note(note_name:str, note_text:str):
    note = {"name": note_name, "text": note_text}
    response = requests.post(f"{FASTAPI_URL}/add", json=note)
    return response.status_code


def search_term(term:str) -> list[str]:
    response = requests.get(f"{FASTAPI_URL}/find?term={term}")
    result = response.json()["results"]
    return result


show_tab, add_tab, search_tab = st.tabs(["Show notes", "Add note", "Search in notes"])

with show_tab:
    name = st.selectbox("All notes", list_notes())
    curr_note = get_note(name)
    if curr_note:
        st.write(curr_note["text"])


with add_tab:
    new_note = st.form("new_note")
    new_note.write("Add a note!")
    name = new_note.text_input("Note name")
    text = new_note.text_input("Note text")
    submit = new_note.form_submit_button("Add note")
    if submit:
        status = add_note(name, text)
        if status == 200:
            new_note.write(f"Successfully added note \"{name}\"")
            time.sleep(1.7)
            st.rerun()

with search_tab:
    st.write("Finds notes whose text contains a given query.")
    search_form = st.form("search")
    query = search_form.text_input("Query:")
    submit = search_form.form_submit_button("Search")
    if submit:
        search_form.write("Relevant notes:")
        results = search_term(query)
        for note in results:
            search_form.write(note)


