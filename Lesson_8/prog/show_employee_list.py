from Lesson_8.input.init_data import load_employees
from Lesson_8.input.init_data import read_data
from Lesson_8.prog.end_program import end_program
def show_employee_list(flag = True):
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