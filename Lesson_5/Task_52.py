# 52.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
list_of_numbers = [1, 2, 3, 5, 1, 5, 3, 10]
result_list_of_numbers = [list_of_numbers[0]]
print(list_of_numbers)

for i in list_of_numbers:
    for j in range(len(result_list_of_numbers)):
        if i == result_list_of_numbers[j]:
            break
        elif j == len(result_list_of_numbers) - 1:
            result_list_of_numbers.append(i)
print(result_list_of_numbers)