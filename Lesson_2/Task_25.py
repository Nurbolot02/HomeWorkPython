# Найти сумму чисел от 1 до А
print('Найти сумму чисел от 1 до А')
number = int(input('Enter the A:'))
i = 1
result = 0
while number >= i:
    result += i
    i += 1
print(result)