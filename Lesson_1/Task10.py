#Напишите программу, которая принимает на вход трёхзначное
#  число и на выходе показывает вторую цифру этого числа.
number = int(input('Enter 3 digit number:'))
number %= 100
number //= 10
print(number)