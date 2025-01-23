import datetime



username=input("Введите имя пользователя: ")

title=[]

for i in range(3):
    input_title=input(f"Введите заголовок {i+1}: ")
    title.append(input_title)

content=input("Введите описание заметки: ")
status=input("Введите статус заметки: ")

created_date=datetime.date.today() #получаем текущую дату
print(f"Дата создания заметки в формате \"дд-мм-гггг\": {created_date.strftime("%d-%m-%Y")}") #выводим текущую дату в нужном формате

issue_date=input("Дата истечения заметки (дедлайн) в формате \"дд-мм-гггг\": ") #получаем от пользователя дату в формате дд-мм-гггг
issue_date=datetime.datetime.strptime(issue_date, "%d-%m-%Y") #конвертируем строку с датой в объект



note_key_list=["username","title","content","status","created_date","issue_date"]
note_element_list=(username,title,content,status,created_date,issue_date)
note=dict(zip(note_key_list, note_element_list))
print(note)

print("\nО заметке")
print(f"Имя пользователя: {username}")
print(f"Заголовок заметки: {title}")
print(f"Описание заметки: {content}")
print(f"Статус заметки: {status}")
print(f"Дата создания заметки в формате \"день-месяц-год\": {created_date.strftime("%d-%m-%Y")}")
print(f"Дата истечения заметки (дедлайн) в формате \"день-месяц-год\": {issue_date.strftime("%d-%m-%Y")}")
print("\n")

for key,value in note.items():
    print(f"{key:15}: {value}")