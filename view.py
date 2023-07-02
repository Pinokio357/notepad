import model

def main_menu():
    print("""Главное меню:
    1.посмотреть список заметок
    2.добавить запись
    3.редактировать запись
    4.удалить запись
    5.посмотреть содержание заметки
    6.сохранить блокнот в файл""")
    choice = input("выберите пункт меню: ")
    if choice.isdigit() and 0 < int(choice) <= 6:
        return int(choice)
    else:
        print("********************* Enter digit from 1 to 6! ***********************")


def show_notes(list, error_message):
    if not list:
        print(error_message)
    else:
        for item in list:
            print(item)

def add_note():
    title = input("введите заголовок заметки:")
    body = input("введите заметку:")
    return {"title": title, "body": body}


def change_note(list, index):
    print("введите новые данные или оставьте поле пустым если не хотите менять")
    note = add_note()
    return {"id": list[index].id, "title": note.get("title") if note.get("title") else list[index].title,
            "body": note.get("body") if note.get("body") else list[index].body}

def del_note():
    print("заметка успешно удалена")

def show_note(np, index, info):
    print("заметка:")
    print(np[index])
    print("содержание:")
    print(info)


def save_to_file():
    print("блокнот сохранен в файл!")

def error():
    print("нет такой заметки!")



