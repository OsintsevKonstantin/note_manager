note={'username':"Konstantin",'title':"note_1",'content':"test",'status':"in work"}
note_status_list=["выполнено","в процессе","отложено"]

while True:
    print("Текущий статус заметки: " + note.get('status'))
    update_note_status_check = input("Изменить статус заметки? да/нет: ")

    if update_note_status_check == "да":

        for value in note_status_list:
            print(f"{note_status_list.index(value) + 1}. {value}")
        note_status = input("Введите номер статуса или \"изменить\" для изменения списка статусов: ")

        if note_status == "изменить":
            add_del_check = input("добавить/удалить статус?: ")
            if add_del_check == "добавить":
                new_note_status = input("Введите новый статус для заметки: ")
                note_status_list.append(new_note_status)
            elif add_del_check == "удалить":
                del_note_status = int(input("Введите номер статуса для удаления: "))
                if 0 < del_note_status <= len(note_status_list):
                    note_status_list.remove(note_status_list[del_note_status-1])
                else:
                    print("Такого статуса нет.")
        elif 0 < int(note_status) <= len(note_status_list):
            note["status"] = note_status_list[int(note_status)-1]
