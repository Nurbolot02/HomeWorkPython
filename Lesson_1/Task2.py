# Даны 2-числа показать какой больше и меньше
number = int(input('Enter 1- number: '))
number2 = int(input('Enter 2- number: '))

if number > number2:
    print(F'{number} больше {number2}')
else:
    print(F'{number2} больше {number}')