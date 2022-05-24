from useFulFutires.IsNumber import isNumber


def end_program(NumberText):
    while True:
        userChoose = isNumber(NumberText)
        if userChoose == 0:
            return False
        elif userChoose == 1:
            return True
