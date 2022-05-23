import pickle
import random
import string

from Lesson_8.input.user_answer import read_user_answer
from useFulFutires.IsNumber import isNumber

employee_list = []

def delete_employee():
    global employee_list
    NumberText = '\n1 - Удалить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    read_user_answer_text = 'Выберите кого хотите удалить по цифре: '
    show_employee_list(False)
    f = True
    while f:
        user_choose = read_user_answer(read_user_answer_text,minNumber=1, maxNumber=len(employee_list)) - 1
        employee_list.pop(user_choose)
        save_employee()
        show_employee_list(False)
        f = end_program(NumberText)
    save_employee()
    print()


def save_employee():
    global employee_list
    path = 'employees.txt'
    try:
        with open(path, 'wb') as data:
            pickle.dump(employee_list, data)
    except:
        print('Ошибка при записи сотрудников в файл')

def add_employee():
    global employee_list
    NumberText = '\n1 - Добавить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        employee_list.append({'Name': input('Имя: '), 'SurName': input('Фамилия: '), 'Position': input('Должность: '), 'Salary': input('Зарплата: ')})
        f = end_program(NumberText)
    save_employee()
    print()

def load_employees(f = True):
    global employee_list
    path = 'employees.txt'
    try:
        with open(path, 'rb') as data:
            employee_list = pickle.load(data)
    except:
        if not f:
            print()
        else:
            print('Нету сотрудников!')
            return False
    return True

def show_employee_list(flag = True):
    global employee_list
    NumberText = '\n1 - Обновить список сотрудников \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    flag2 = load_employees()
    if flag2:
        print('\nСписок сотрудников')
    if flag == False:
        read_data()
    else:
        while f:
            read_data()
            f = end_program(NumberText)


def read_data():
    global employee_list
    counter = 1
    print()
    for i in employee_list:
        print(f'{counter} - ', end='')
        for key, value in i.items():
            print(f'{key}: {value}', end=', ')
        print()
        counter +=1
    print(f'Обшее количество сотрудников {len(employee_list)}')

def generate_random_employee():
    global contact_list
    f = True
    NumberText = '\n1 - Добавить еще рандомного сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    while f:
        read_user_answer_text = 'Сколько рандомных сотрудников вы хотите добавить?: '
        count = read_user_answer(read_user_answer_text, maxNumber=10000)
        for i in range(count):
            employee_list.append({'Name': generate_random_string(8), 'SurName': generate_random_string(8), 'Position': generate_random_string(8), 'Salary': generate_random_phone_number()})
        f = end_program(NumberText)
    save_employee()



def generate_random_string(length = 8):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_phone_number(length= 8, minNumber = 0, maxNumber = 9):
    result = '+'
    for i in range(length):
        result += str(random.randint(minNumber, maxNumber))
    return result


def end_program(NumberText):
    while True:
        userChoose = isNumber(NumberText)
        if userChoose == 0:
            return False
        elif userChoose == 1:
            return True

