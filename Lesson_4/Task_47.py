# 47.	Строка содержит набор чисел. Показать большее и меньшее число
print('47.	Строка содержит набор чисел. Показать большее и меньшее число')
number = input('Enter the number: ')
number = number.split()
print(f'max = {max(number)}  min = {min(number)}')