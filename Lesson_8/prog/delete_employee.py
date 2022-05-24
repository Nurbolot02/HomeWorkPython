from Lesson_8.prog.show_employee_list import show_employee_list
from Lesson_8.prog.save_employee import save_employee
from Lesson_8.prog.end_program import end_program
from Lesson_8.input.user_answer import read_user_answer
def delete_employee(employee_list):
    NumberText = '\n1 - Удалить еще сотрудника \n0 - Выйти в главное меню \nВыберите операцию: '
    read_user_answer_text = 'Выберите кого хотите удалить по цифре: '
    show_employee_list(False)
    f = True
    while f:
        user_choose = read_user_answer(read_user_answer_text,minNumber=1, maxNumber=len(employee_list)) - 1
        employee_list.pop(user_choose)
        save_employee(employee_list)
        show_employee_list(False)
        f = end_program(NumberText)
    print()
