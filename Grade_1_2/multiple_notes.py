import datetime

note_status_list=["выполнено","в процессе","отложено"]
data_notes = []

def add_titles_loop():
    title = []  # список с заголовками
    title_num = 0  # номер заголовка

    count_title = int(input("Введиче число заголовков: "))

    while True:

        while title_num < count_title:
            input_title = input(f"Введите заголовок {title_num + 1}: ")
            title_num += 1
            title.append(input_title)

        repeat_check = input("Добавить ещё заголовки? (да/нет): ")
        if repeat_check == "да":
            count_title += int(input("Введиче число заголовков: "))
            continue
        elif repeat_check == "нет":
            break

    return title


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




while True:

    add_print = input("добавить/вывести заметку(и)?: ")

    if add_print == "добавить":
        note = {
            "username" : input("Введите имя пользователя: "),
            "title" : add_titles_loop(),
            "content" : input("Введите описание заметки: "),
            "status" : update_status(),
            "created_date" : datetime.date.today(),  # получаем текущую дату
            "issue_date" : add_issue_date()
        }

        data_notes.append(note)
    elif add_print == "вывести":
        for note in data_notes:
            for key, value in note.items():
                print(f"{key:15}: {value}")
            if note["created_date"] > note["issue_date"]:  # если дата создания позже введенной даты
                interval = note["created_date"] - note["issue_date"]
                print(f"Дедлайн истёк {interval.days} дней назад")
            elif note["created_date"] < note["issue_date"]:
                interval = note["issue_date"] - note["created_date"]
                print(f"До конца дедлайна {interval.days} дней")
            elif note["created_date"] == note["issue_date"]:
                print("Дедлайн сегодня")

