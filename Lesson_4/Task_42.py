# 42.	Найти сумму чисел списка стоящих на нечетной позиции
print('42.	Найти сумму чисел списка стоящих на нечетной позиции')
list_of_numbers = [1,5,5,6,9,9,9,5,8,7,3]
print(list_of_numbers)
result = 0
for i in range(1, len(list_of_numbers), 2):
    result += list_of_numbers[i]
print(result)