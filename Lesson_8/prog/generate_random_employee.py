from Lesson_8.input.user_answer import read_user_answer
from Lesson_8.prog.generate_random_phone_number import generate_random_phone_number
from Lesson_8.prog.generate_random_string import generate_random_string
from Lesson_8.prog.end_program import end_program
from Lesson_8.prog.save_employee import save_employee

def generate_random_employee(employee_list):
    f = True
    NumberText = '\n1 - Добавить еще рандомного сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    while f:
        read_user_answer_text = 'Сколько рандомных сотрудников вы хотите добавить?: '
        count = read_user_answer(read_user_answer_text, maxNumber=1000000)
        for i in range(count):
            employee_list.append({'Name': generate_random_string(8), 'SurName': generate_random_string(8), 'Position': generate_random_string(8), 'Salary': generate_random_phone_number()})
        f = end_program(NumberText)
    save_employee(employee_list)

