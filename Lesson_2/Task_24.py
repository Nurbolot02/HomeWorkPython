# Найти кубы чисел от 1 до N
number = int(input('Enter the N:'))
i = 1
degree = 3
while number >= i:
    print(i ** degree, end=' ')
    i += 1