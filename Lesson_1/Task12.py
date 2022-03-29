# 12. Напишите программу, которая будет принимать на вход два числа и выводить,
# является ли второе число кратным первому. Если число 2 не кратно числу 1,
# то программа выводит остаток от деление.
#     34, 5 -> не кратно, остаток 4
#     16, 4 -> кратно
number = int(input('Enter 1- number: '))
number2 = int(input('Enter 2- number: '))
if number % number2 == 0:
    print("Multiplicity")
else:
    print(f"Not multiple, reminder {number % number2}")