# 16. Напишите программу, которая принимает на вход два числа и
#             проверяет, является ли второе число квадратом первого.
#             5, 25  ->  да
#             -4, 16  ->  да
#             25, 5  ->  нет
#             8,9  ->  нет
number = int(input('Enter 1- number: '))
number2 = int(input('Enter 2- number: '))
if number * number == number2:
    print(True)
else:
    print(False)