# Подсчитать сумму цифр в числе
print('Подсчитать сумму цифр в числе')
number = int(input('Enter the number : '))
result = 0
while number > 0:
    result += number % 10
    number //= 10
print(f'Sum numbers = {result}')