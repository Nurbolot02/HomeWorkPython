# Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
#             645 -> 5
#             78 -> третьей цифры нет
#             32679 -> 6
number = input('Enter the number: ')
if len(number) > 99:
    print(number[2])
else:
    print("No third digit")