# 36	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму
print('36 Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму')
number = int(input('Enter the number: '))
list_of_numbers = []
result = 0
for n in range(1, number + 1):
    list_of_numbers.append((1 + 1 / n) ** n)
    result += (1 + 1 / n) ** n
print(result)