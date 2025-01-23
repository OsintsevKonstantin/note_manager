data_notes=[
    {
        'username' : '1',
        'title' : '1',
        'content' : '1'
    },

    {
        'username' : '1',
        'title' : '2',
        'content' : '2'
    },

    {
        'username' : '2',
        'title' : '3',
        'content' : '3'
    },

    {
        'username' : '2',
        'title' : '4',
        'content' : '4'
    },

    {
        'username' : '3',
        'title' : '3',
        'content' : '5'
    },

    {
        'username' : '4',
        'title' : '4',
        'content' : '6'
    },

    {
        'username' : '1',
        'title' : '5',
        'content' : '7'
    },

]

while True:

    for note in data_notes:
        print(note)

    removal_criteria_selector = input('По какому параметру удалить заметку? (имя/заголовок): ')
    if removal_criteria_selector == 'имя':
        removal_criteria = input('Введите имя пользователя: ')
        removal_criteria_true = 0
        for note in data_notes:
            if removal_criteria == note['username']:
                print(note)
                removal_criteria_true+=1

        if removal_criteria_true == 0:
            print('Таких заметок нет')
        else:
            approval_delete_notes = input('Удалить эти заметки? (да/нет): ')
            if approval_delete_notes == 'да':
                delete_notes_collection = []
                iteration = 0
                for note in data_notes:
                    if removal_criteria == note['username']:
                        delete_notes_collection.append(data_notes.index(note))
                for element_delete_collection in reversed(delete_notes_collection):
                    data_notes.remove(data_notes[element_delete_collection])




    elif removal_criteria_selector == 'заголовок':
        removal_criteria = input('Введите заголовок: ')
        removal_criteria_true = 0
        for note in data_notes:
            if removal_criteria == note['title']:
                print(note)
                removal_criteria_true += 1

        if removal_criteria_true == 0:
            print('Таких заметок нет')
        else:
            approval_delete_notes = input('Удалить эти заметки? (да/нет): ')
            if approval_delete_notes == 'да':
                delete_notes_collection = []
                for note in data_notes:
                    if removal_criteria == note['title']:
                        delete_notes_collection.append(data_notes.index(note))
                for element_delete_collection in reversed(delete_notes_collection):
                    data_notes.remove(data_notes[element_delete_collection])

