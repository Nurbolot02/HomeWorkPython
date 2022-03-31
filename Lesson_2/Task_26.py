# Возведите число А в натуральную степень B используя цикл
import math
import time

import numpy as np

a = int(input('Enter the A:'))
b = int(input('Enter the B:'))
i = 1
result = 1
# start = time.process_time()
# while b >= i:
#     result *= a
#     i += 1
# print(f'while {time.process_time() - start} ms {a} ^ {b} == {result} ')

start = time.process_time()
result = a ** b
print(f'** - {time.process_time() - start} ms {a} ^ {b} == {result} ')


start = time.process_time()
result = pow(a, b)
print(f'Math.Pow - {time.process_time() - start} ms {a} ^ {b} == {result} ')


