from useFulFutires.IsNumber import isNumber


def Addition(a, b):
    return a + b
def Multiplication(a, b):
    return a * b
def exponentiation(a, b):
    return a ** b
def division(a, b):
    return a / b
def division_without_remainder_from_division(a, b):
    return a // b
def Subtraction(a, b):
    return a - b
def math(operation, a, b):
    return operation(a, b)

mathOper = 0
mathOperText = 'Выберите операцию: '
print('1-сложение \n2-вычитание \n3-Умножение \n4-Деление \n5-Возведение в степень \n6-деление без остатка')
while True:
    mathOper = isNumber(mathOperText)
    if(mathOper > 0 and mathOper <= 6):
        break
    else:
        print('Выберите одного из операторов!')

aText = 'Введите A: '
a = isNumber(aText)
bText = 'Введите B: '
b = isNumber(bText)

switcher = {
    1 : Addition,
    2 : Subtraction,
    3 : Multiplication,
    4 : division,
    5 : exponentiation,
    6 : division_without_remainder_from_division
    }
switcherMath = {
    1 : '+',
    2 : '-',
    3 : '*',
    4 : '/',
    5 : 'в степени',
    6 : 'деление без остатка на'
            }
result = math(switcher[mathOper], a, b)
print(f'{a} {switcherMath[mathOper]} {b} = {result}')
