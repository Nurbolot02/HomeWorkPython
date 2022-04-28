# 3. Найти НОК двух чисел
from useFulFutires.IsNumber import isNumber

number1Text = 'Enter a: '
number1 = isNumber(number1Text)
number2Text = 'Enter b: '
number2 = isNumber(number2Text)

c = max(number1, number2)
k = 1

while True:
    if (((c * k) % number1) == 0 and ((c * k) % number2) == 0):
        print(c * k)
        break
    k += 1

