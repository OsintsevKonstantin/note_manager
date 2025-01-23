import datetime

created_date = datetime.datetime.today().date()  #получаем текущую дату

print(f'Текущая дата в формате "дд-мм-гггг": {created_date.strftime("%d-%m-%Y")}')
issue_date = input(
    'Дата истечения заметки (дедлайн) в формате "дд-мм-гггг": ')  # получаем от пользователя дату в формате дд-мм-гггг
issue_date = datetime.datetime.strptime(issue_date, "%d-%m-%Y").date()  #конвертируем строку с датой в объект

if created_date > issue_date:  #если дата создания позже введенной даты
    interval = created_date - issue_date
    print(f"Дедлайн истёк {interval.days} дней назад")
elif created_date < issue_date:
    interval = issue_date - created_date
    print(f"До конца дедлайна {interval.days} дней")
elif created_date == issue_date:
    print("Дедлайн сегодня")
