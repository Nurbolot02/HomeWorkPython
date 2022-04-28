# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0
from sympy import parse_expr, symbols

path1 = 'Polynom1.txt'
path2 = 'Polynom2.txt'
with open(path1, 'r') as file:
    mNumber = file.read()
with open(path2, 'r') as file:
    mNumber2 = file.read()
print(f'({mNumber}) + ({mNumber2})')
x = symbols('x')
mNumber = parse_expr(mNumber.replace('^', '**'), local_dict={'x': x})
mNumber2 = parse_expr(mNumber2.replace('^', '**'), local_dict={'x': x})
sumMNumbers = mNumber + mNumber2
print(f'({mNumber}) + ({mNumber2})')
print(f'{mNumber} + {mNumber2}')
print(sumMNumbers)

