# Показат числа от - N до N
from useFulFutires.IsNumber import isNumber

numText = 'Введите n: '
number = isNumber(numText)

for i in range(-number, number + 1):
    print(f'{i}', end=' ')