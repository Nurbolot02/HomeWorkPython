from Lesson_7.Phone_book.out import menu
from Lesson_7.Phone_book.prog.Contact import add_contact, show_contacts, del_contact, find_contact
from Lesson_7.Phone_book.input import user_answer


def start():
    while True:
        menu.get_menu()
        user_select = user_answer.read_user_answer()
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            add_contact()
        elif user_select == 2:
            del_contact()
        elif user_select == 3:
            show_contacts()
        elif user_select == 4:
            find_contact()
