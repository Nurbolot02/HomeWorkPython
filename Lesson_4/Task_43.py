# 43.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
# 44.	 [2, 3, 5, 6] => [12, 15]
list_of_numbers = [2, 3, 4, 5, 6]
#product_of_numbers = [list_of_numbers[i] * list_of_numbers[len(list_of_numbers) - 1 -i] for i in range(len(list_of_numbers) // 2)]
product_of_numbers = []
length = len(list_of_numbers) // 2 if len(list_of_numbers) % 2 == 0 else len(list_of_numbers) // 2 + 1
for i in range(length):
    product_of_numbers.append(list_of_numbers[i] * list_of_numbers[len(list_of_numbers) - 1 -i])
print(product_of_numbers)