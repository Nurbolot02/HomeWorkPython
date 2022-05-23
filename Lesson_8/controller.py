from Lesson_8.out.menu import get_menu
from Lesson_8.input import user_answer
from Lesson_8.prog.employee import add_employee, show_employee_list, generate_random_employee, delete_employee, load_employees
def start():
    while True:
        load_employees(False)
        get_menu()
        user_select = user_answer.read_user_answer()
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            add_employee()
        elif user_select == 2:
            show_employee_list()
        elif user_select == 3:
            generate_random_employee()
        elif user_select == 4:
            delete_employee()