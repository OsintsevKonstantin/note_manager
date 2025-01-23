from collections import OrderedDict
import datetime


data_notes = []
note_status_list=["выполнено","в процессе","отложено"]

def print_note(note): #Вывод одной заметки с форматированием
    for key, value in note.items():
        print(f"{key:12}: {value}")
    if note["created_date"] > note["issue_date"]:  # если дата создания позже введенной даты
        interval = note["created_date"] - note["issue_date"]
        print(f"Дедлайн истёк {interval.days} дней назад")
    elif note["created_date"] < note["issue_date"]:
        interval = note["issue_date"] - note["created_date"]
        print(f"До конца дедлайна {interval.days} дней")
    elif note["created_date"] == note["issue_date"]:
        print("Дедлайн сегодня")
    print('----------------------------------------------------#')

def add_titles_loop(): #Добавление заголовков
    title = []  # список с заголовками

    while True:
        input_title = input("Введите заголовок: ")#Вводим хотябы 1 заголовок
        if input_title.replace(' ','') != '':
            title.append(input_title)
            break

    while True:
        input_title = input("Введите заголовок (оставьте поле пустым для завершения): ")
        if input_title.replace(' ','') != '':#проверяем чтоб небыло просто пробелов
            title.append(input_title)
        else:
            break
    return title

def delete_note():
    removal_criteria_selector = input('По какому параметру удалить заметку? (имя/заголовок): ')
    if removal_criteria_selector == 'имя':
        removal_criteria = input('Введите имя пользователя: ')
        removal_criteria_true = False #Проверка наличия совпадающих с запросом заметок
        for note in data_notes:
            if removal_criteria == note['username']:
                print_note(note)
                removal_criteria_true = True

        if removal_criteria_true == False:
            print('Таких заметок нет')

        else:
            approval_delete_notes = input('Удалить эти заметки? (да/нет): ')
            if approval_delete_notes == 'да':
                delete_notes_collection = []
                for note in data_notes:
                    if removal_criteria == note['username']:
                        delete_notes_collection.append(data_notes.index(note))
                delete_notes_collection = list(OrderedDict.fromkeys(delete_notes_collection))#Удаление дубликатов в списке на всякий случай
                for element_delete_collection in reversed(delete_notes_collection):
                    data_notes.remove(data_notes[element_delete_collection])

    elif removal_criteria_selector == 'заголовок':
        removal_criteria = input('Введите заголовок: ')
        removal_criteria_true = False
        for note in data_notes:
            for title in note['title']:
                if removal_criteria == title:
                    print_note(note)
                    removal_criteria_true = True

        if removal_criteria_true == False:
            print('Таких заметок нет')

        else:
            approval_delete_notes = input('Удалить эти заметки? (да/нет): ')
            if approval_delete_notes == 'да':
                delete_notes_collection = []
                for note in data_notes:
                    for title in note['title']:
                        if removal_criteria == title:
                            delete_notes_collection.append(data_notes.index(note))
                delete_notes_collection = list(OrderedDict.fromkeys(delete_notes_collection))  # Удаление дубликатов в списке на всякий случай
                for element_delete_collection in reversed(delete_notes_collection):
                    data_notes.remove(data_notes[element_delete_collection])

def update_status():

    while True:

        for value in note_status_list:
            print(f"{note_status_list.index(value) + 1}. {value}")
        note_status = input('Введите номер статуса или "изменить" для изменения списка статусов: ')

        if note_status == "изменить":
            add_del_check = input("добавить/удалить статус?: ")
            if add_del_check == "добавить":
                new_note_status = input("Введите новый статус для заметки: ")
                note_status_list.append(new_note_status)
            elif add_del_check == "удалить":
                del_note_status = int(input("Введите номер статуса для удаления: "))
                if 0 < del_note_status <= len(note_status_list):
                    note_status_list.remove(note_status_list[del_note_status - 1])
                else:
                    print("Такого статуса нет.")
        elif 0 < int(note_status) <= len(note_status_list):
            return note_status_list[int(note_status) - 1]

def add_issue_date():

    issue_date = input("Дата истечения заметки (дедлайн) в формате \"дд-мм-гггг\": ")  # получаем от пользователя дату в формате дд-мм-гггг
    issue_date = datetime.datetime.strptime(issue_date, "%d-%m-%Y").date()  # конвертируем строку с датой в объект
    return issue_date

#Начало программы
print('Добро пожаловать в менеджер заметок.')
while True:
    select_action = input('1-вывести заметки | 2-добавить заметку | 3-удалить заметку | 4-выход : ')
    if select_action == '1':
        if not data_notes:
            print('Пока заметок нет.')
        else:
            for note in data_notes:
                print_note(note)

    elif select_action == '2':
        note = {
            "username": input("Введите имя пользователя: "),
            "title": add_titles_loop(),
            "content": input("Введите описание заметки: "),
            "status": update_status(),
            "created_date": datetime.date.today(),  # получаем текущую дату
            "issue_date": add_issue_date()
        }
        data_notes.append(note)

    elif select_action == '3':
        delete_note()
    elif select_action == '4':
        break

