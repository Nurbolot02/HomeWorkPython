
def isNumber():
    while True:
        number = input('Enter the number: ')
        if number.isdigit():
            return int(number)
def isNumber(string):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)