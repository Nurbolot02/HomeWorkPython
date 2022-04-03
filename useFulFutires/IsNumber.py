
def isNumber():
    while True:
        number = input('Enter the number: ')
        if number.isdigit():
            return int(number)
