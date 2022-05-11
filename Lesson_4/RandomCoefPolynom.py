# 53. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

from useFulFutires.IsNumber import isNumber

k = isNumber()
count = k
randomKoef = [random.randint(0, 100) for i in range(k+1)]

resultT = ""
for i in range(k):
    if i == k-1:
        resultT += str(randomKoef[i]) + '*x + '
        resultT += str(randomKoef[i+1])
        break
    else:
        resultT += str(randomKoef[i]) + f'*x**{count} + '
    count -= 1

resultT += ' = 0'
print(resultT)
path = 'randomCoefPolynom.txt'

with open(path, 'w') as d:
    d.write(resultT)