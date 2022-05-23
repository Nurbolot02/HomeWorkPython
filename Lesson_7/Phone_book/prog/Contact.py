from Lesson_7.Phone_book.input.user_answer import get_user_name, get_phone_number
from useFulFutires.IsNumber import isNumber

contact_id = 1
contact_list = []
def add_contact():
    global contact_id, contact_list
    NumberText = '\n1 - Добавить еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nДобавить контакт')
        contact_list.append({contact_id: {'Name': get_user_name(), 'Phone Number': get_phone_number()}})
        contact_id += 1

        f = end_program(NumberText)


def show_contacts():
    global contact_list
    NumberText = '\n1 - Обновить список контактов \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True

    while f:
        print('\nСписок контактов ')
        for i in contact_list:
            for key, value in i.items():
                print(f'{key}: {value["Name"]} - {value["Phone Number"]}')
        print()
        f = end_program(NumberText)


def del_contact():
    print('\nУдалить контакт ')


def find_contact():
    print('\nНайти номер по имени')

def end_program(NumberText):
    while True:
        userChoose = isNumber(NumberText)
        if userChoose == 0:
            return False
        elif userChoose == 1:
            return True
