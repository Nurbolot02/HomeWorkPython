from Lesson_8.out.menu import get_menu
from Lesson_8.input import user_answer, init_data
from Lesson_8.prog import add_employee, show_employee_list, generate_random_employee, delete_employee
from Lesson_8.prog.find_employee import find_employee
def start():
    while True:
        employee_list = init_data.init()
        get_menu()
        user_select = user_answer.read_user_answer()
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            add_employee.add_employee(employee_list)
        elif user_select == 2:
            show_employee_list.show_employee_list()
        elif user_select == 3:
            generate_random_employee.generate_random_employee(employee_list)
        elif user_select == 4:
            find_employee(employee_list)
        elif user_select == 5:
            delete_employee.delete_employee(employee_list)
