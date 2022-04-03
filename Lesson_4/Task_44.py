# 44.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
import time

print('44.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. '
      'Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19')
list_of_float_numbers = [1.1, 1.2, 3.1, 5, 10.01]
float_numbers = []
for i in list_of_float_numbers:
      if round(i % 1, 2) > 0:
            float_numbers.append(round(i % 1, 2))
print(list_of_float_numbers)
print(float_numbers)
start = time.process_time()
max = max(float_numbers)
min = min(float_numbers)
print(f'{start}ms {max - min}')
# 0.046875ms 0.19 Sort metod


