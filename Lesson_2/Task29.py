# Написать программу вычисления произведения чисел от 1 до N
print('Написать программу вычисления произведения чисел от 1 до N')
number = int(input('Enter the number: '))
i = 1
result = 1
while number >= i:
    result *= i
    i += 1
print(f'Произведение чисел от 1 до {number} == {result}')