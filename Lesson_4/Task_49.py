# 49.	Найти НОК двух чисел
import math

from useFulFutires.IsNumber import isNumber

print('49.	Найти НОК двух чисел')
n1Str = 'Enter 1-number: '
n = isNumber(n1Str)
n2Str = 'Enter 2-number: '
m = isNumber(n2Str)

print((n * m) // math.gcd(n, m)) # gcd - greatest common devisor