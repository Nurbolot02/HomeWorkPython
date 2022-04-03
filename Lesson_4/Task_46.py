# 46.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
print('46.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов')
number = int(input('Enter the number : '))
list_of_fibonacci = [1, 1]
list_of_fibonacci_minus = [-1, -1]
for i in range(2, 1 + number):
    list_of_fibonacci.append(list_of_fibonacci[i - 2] + list_of_fibonacci[i - 1])
    list_of_fibonacci_minus.insert(0, list_of_fibonacci[i] * -1)
list_of_fibonacci_minus.append(list_of_fibonacci)
print(list_of_fibonacci_minus)