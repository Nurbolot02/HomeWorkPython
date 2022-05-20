from useFulFutires.IsNumber import isNumber


Addition = lambda a, b: a + b
Multiplication = lambda  a, b: a * b
exponentiation = lambda  a, b: a ** b
division = lambda  a, b: a / b
division_without_remainder_from_division = lambda  a, b: a // b
Subtraction= lambda  a, b: a - b
math = lambda  operation, a, b: operation(a, b)

# def math(operation, a, b):
#     return operation(a, b)

mathOper = 0
mathOperText = 'Выберите операцию: '
print('Добро пожаловать в калькулятор который написал Nurbolot\n'
      '1-сложение \n2-вычитание \n3-Умножение \n4-Деление \n5-Возведение в степень \n6-деление без остатка')
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
    5 : '**',
    6 : '//'
            }
result = math(switcher[mathOper], a, b)
print(f'{a} {switcherMath[mathOper]} {b} = {result}')