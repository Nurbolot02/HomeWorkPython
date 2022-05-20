# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
number = input(print('Введите арифметического выражения через пробел:'))
number = number.split()
print(number)
result_1 = [number[i] for i in range(len(number)) if number[i] == '*' or number[i] == '/']
result_2 = [number[i] for i in range(len(number)) if number[i] == '+' or number[i] == '-']
print(result_1)
for i in range(len(number)):
    if number[i] == '*':
        mult = int(number[i - 1]) * int(number[i + 1])
    elif number[i] == '/':
        mult = int(number[i - 1]) / int(number[i + 1])
