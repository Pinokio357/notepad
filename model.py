import datetime
import json

import view

notes_objects = []
path = "note.json"


class Note:
    id = 0
    title = "title"
    body = "body"

    def __init__(self, id, title, body, date = None):
        self.id = id
        self.title = title
        self.body = body
        if date is None:
            self.date = datetime.datetime.now().strftime("%d %m %Y %H %M %S")
        else:
            self.date = date


    def change_title(self, message):
        self.title = message
        self.date = datetime.datetime.now().strftime("%d %m %Y %H %M %S")

    def change_body(self, message):
        self.body = message
        self.date = datetime.datetime.now().strftime("%d %m %Y %H %M %S")

    def __str__(self):
        return f"note number: {self.id}; date: {self.date}; title: {self.title};"

    def dict(self):
        if isinstance(self.date, str):
            return {"id": self.id, "date": self.date, "title": self.title, "body": self.body}
        else:
            return {"id": self.id, "date": self.date.strftime("%d %m %Y %H %M %S"), "title": self.title, "body": self.body}





def open_notepad():
    with open(path, "r", encoding="utf8")as file:
        data = json.load(file)
        for i in data:
            notes_objects.append(Note(i["id"], i["title"], i["body"], datetime.datetime.strptime(i["date"], "%d %m %Y %H %M %S")))



def get_notepad():
    return notes_objects

def get_number(message, error_message, max):
    control = False
    while control == False:
        test = input(message)
        if test.isdigit() == True:
            if int(test) <= max:
                result = int(test)
                control = True
            else:
                view.error()
        else:
            print(error_message)

    return result

def add_note(dict):
    id = max_id(notes_objects) + 1
    note = Note(id, dict.get("title"), dict.get("body"))
    notes_objects.append(note)



def max_id(list):
    max = 0
    for element in list:
        if element.id > max:
            max = element.id

    return  max


def change_note(notes_objects, dict, index):
    note = Note(dict.get("id"), dict.get("title"), dict.get("body"))
    notes_objects[index] = note


def find_index_in_list(notes_objects, number):
    flag = False
    while flag == False:
        index = None
        i = 0
        for note in notes_objects:
            if note.id == number:
                index = i
                flag = True
            else:
                i += 1
        if index:
            return index
        else:
            view.error()


def del_note(notes_objects, index):
    notes_objects.pop(index)


def show_note(notes_objects, index):
    return notes_objects[index].body


def save_to_file(notes_objects):
    notes_list = []
    for note in notes_objects:
        notes_list.append(note.dict())
    with open("note.json", "w", encoding="utf8", ) as file:
        json.dump(notes_list, file, indent=2, ensure_ascii=False)








