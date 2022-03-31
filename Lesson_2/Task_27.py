# Определить количество цифр в числе
print('Определить количество цифр в числе')
number = int(input('Enter the number: '))
count = 0
while number > 0:
    number //= 10
    count += 1
print(f'count = {count}')