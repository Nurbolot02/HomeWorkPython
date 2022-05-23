import random
import string

from Lesson_7.Phone_book.input.user_answer import get_user_name, get_phone_number, read_user_answer
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


def show_contacts(is_end_prog = False):
    global contact_list
    NumberText = '\n1 - Обновить список контактов \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True

    if is_end_prog:
        print('\nСписок контактов ')
        for i in contact_list:
            for key, value in i.items():
                print(f'{key}: {value["Name"]}: {value["Phone Number"]}')
        print()
    else:
        while f:
            print('\nСписок контактов ')
            for i in contact_list:
                for key, value in i.items():
                    print(f'{key}: {value["Name"]}: {value["Phone Number"]}')
            print()
            f = end_program(NumberText)


def del_contact():
    global contact_list, contact_id
    NumberText = '\n1 - Удалить еще контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        print('\nУдалить контакт ')
        show_contacts(True)
        read_user_answer_text = 'Выберите цифру контакта: '
        user_answer = read_user_answer(read_user_answer_text,minNumber= 1, maxNumber=len(contact_list)) - 1
        contact_list.pop(user_answer)
        show_contacts(True)
        f = end_program(NumberText)


def find_contact():
    print('\nНайти номер по имени')


def end_program(NumberText):
    while True:
        userChoose = isNumber(NumberText)
        if userChoose == 0:
            return False
        elif userChoose == 1:
            return True


def generate_random_contact():
    global contact_id, contact_list
    f = True
    NumberText = '\n1 - Добавить еще рандомный контакт \n0 - Выйти в главное меню \nВыберите операцию: '
    while f:
        read_user_answer_text = 'Сколько рандомных контактов вы хотите добавить?: '
        count = read_user_answer(read_user_answer_text, maxNumber=10000)
        for i in range(count):
            contact_list.append(  {contact_id: {'Name': generate_random_string(8), 'Phone Number': generate_random_phone_number()}})
            contact_id += 1
        f = end_program(NumberText)



def generate_random_string(length = 8):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_phone_number(length= 8, minNumber = 0, maxNumber = 9):
    result = '+'
    for i in range(length):
        result += str(random.randint(minNumber, maxNumber))
    return result

