import random
import string

from Lesson_8.input.user_answer import read_user_answer
from useFulFutires.IsNumber import isNumber

employee_list = []

def save_employee():
    path = 'employees.txt'
    with open(path, 'w') as data:
        for i in employee_list:
            data.write(f'{i} \n')

def add_employee():
    global employee_list
    NumberText = '\n1 - Добавить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    while f:
        employee_list.append({'Name': input('Имя: '), 'SurName': input('Фамилия: '), 'Position': input('Должность: '), 'Salary': input('Зарплата: ')})
        f = end_program(NumberText)
    save_employee()
    print()


def show_employee_list():
    global employee_list
    NumberText = '\n1 - Обновить список сотрудников \n0 - Выйти в главное меню \nВыберите операцию: '
    f = True
    print('\nСписок сотрудников')
    while f:
        for i in employee_list:
            for key, value in i.items():
                print(f'{key}: {value}')
            print(f'{"-"* 50}')
        f = end_program(NumberText)
    print()

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

