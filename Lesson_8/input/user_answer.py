from useFulFutires.IsNumber import isNumber

user_answer = 0


def read_user_answer(user_answer_text = 'Выберите операцию: ', minNumber = 0, maxNumber = 3):
    global user_answer
    while True:
        user_answer = isNumber(user_answer_text)
        if user_answer >= minNumber and user_answer <= maxNumber:
            break
    return user_answer


def get_user_name():
    return input('Введите имя:')


def get_phone_number():
    return input('номер телефона:')