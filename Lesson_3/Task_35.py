# 35.	Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
number = int(input('Enter the number: '))
for i in range(1,number+1):
    print(i * i, end=' ')