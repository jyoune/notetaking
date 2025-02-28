from dataclasses import dataclass

@dataclass
class Note:
    """Note class that contains a name field and a text field"""
    name: str
    text: str

    def text(self) -> str:
        return self.text


class NoteTaker:
    def __init__(self, directory='data'):
        self.directory = directory
        self.notes = dict()

    def add(self, name, text):
        self.notes[name] = Note(name, text)

    def __getitem__(self, key):
        return self.notes[key]

    def get_notes(self):
        return list(self.notes.keys())

    def find(self, query):
        return [name for name in self.notes if query in self.notes[name].text]
