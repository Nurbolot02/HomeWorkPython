def isNumber(string = 'Enter the number: '):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)
