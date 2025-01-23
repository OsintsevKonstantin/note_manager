import datetime

username="user"
title="title"
content="description"
status="work"
created_date=datetime.date(2024,11,14)
issue_date=datetime.date(2024,12,14)

print(f"Имя пользователя: {username}")
print(f"Заголовок заметки: {title}")
print(f"Описание заметки: {content}")
print(f"Статус заметки: {status}")
print(f"Дата создания заметки в формате \"день-месяц-год\": {created_date.strftime("%d-%m-%Y")}")
print(f"Дата истечения заметки (дедлайн) в формате \"день-месяц-год\": {issue_date.strftime("%d-%m-%Y")}")