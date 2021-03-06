# в файле хранится числа, нужно выбрать четные из них и
# и составить список пар (число: квадрат числа)
# пример:
# 1 2 3 5 8 15 23 38
# получить:
# [(2,4), (8m64), (38, 1444)]

path = 'file.txt'
with open(path, 'r') as data:
    for e in data:
        number_text = list(map(int, e.split()))
        list_of_numbers = [(i, i**2) for i in number_text if i % 2 == 0]
with open(path, 'a') as d:
    d.write(f'\n{list_of_numbers}')
print(list_of_numbers)


# path = 'file.txt'
# numbers_text = ''
# with open(path, 'r') as data:
#     for i input_data data:
#         numbers_text = i.split()
# list_of_numbers = [int(i) for i input_data numbers_text]
# result = [(i, i ** 2) for i input_data list_of_numbers if i % 2 == 0]
# print(result)