import model
import view


def start():
    model.open_notepad()
    np = model.get_notepad()
    flag = False

    while flag == False:
        choise = view.main_menu()
        match choise:
            case 1:

                view.show_notes(np, "блокнот пуст или не открыт")
            case 2:
               temp = view.add_note()
               model.add_note(temp)

            case 3:

                view.show_notes(np, "блокнот пуст или не открыт")
                number = model.get_number("введите индекс изменяемой заметки:", "введите верный номер!", len(np))
                index = model.find_index_in_list(np, number)
                temp = view.change_note(np, index)
                model.change_note(np, temp, index)

            case 4:
                view.show_notes(np, "блокнот пуст или не открыт")
                number = model.get_number("введите индекс удаляемой заметки: ", "введите верный номер!", len(np))
                index = model.find_index_in_list(np, number)
                model.del_note(np, index)
                view.del_note()
            case 5:
                view.show_notes(np, "блокнот пуст или не открыт")
                number = model.get_number("введите индекс заметки, которую хотите посмотреть: ", "введите верный номер!", len(np))
                index = model.find_index_in_list(np, number)
                info = model.show_note(np, index)
                view.show_note(np, index, info)
            case 6:
                model.save_to_file(np)
                view.save_to_file()
                flag = True



