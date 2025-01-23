title = [] #список с заголовками
title_num = 0 #номер заголовка

count_title = int(input("Введиче число заголовков: "))

while True:

    while title_num < count_title:
        input_title=input(f"Введите заголовок {title_num+1}: ")
        title_num+=1
        title.append(input_title)
    repeat_check = input("Добавить ещё заголовки? (да/нет): ")
    if repeat_check == "да":
        count_title +=  int(input("Введиче число заголовков: "))
        continue
    elif repeat_check == "нет":
        print(title)
        break
