# Найти максимальное из 3 - чисел
numbers = []
count = 1
for i in range(3):
    numbers.append(int(input(f'Enter {count}- number: ')))
    count += 1
min = numbers[0]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f'max number: {max} min number: {min}')