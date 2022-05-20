# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
import random

from useFulFutires.Factor import factor

n = int(input('Enter the N: '))
randomNumbers = [random.randint(1, n**2) for i in range(n)]
result = [list(map(lambda x: factor(x), randomNumbers))]
print(result)