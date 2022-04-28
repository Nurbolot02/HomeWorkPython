# 53. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

from useFulFutires.IsNumber import isNumber

k = isNumber()
mNumbers = [f'*x**{k} + ','*x + ',' = 0']
randomKoef = [random.randint(0, 100) for i in range(len(mNumbers))]

resultT = ""
for i in range(len(randomKoef)):
    resultT += str(randomKoef[i]) + mNumbers[i]
    print(f'{randomKoef[i]}{mNumbers[i]}',end='')
path = 'randomCoefPolynom.txt'

with open(path, 'w') as d:
    d.write(resultT)