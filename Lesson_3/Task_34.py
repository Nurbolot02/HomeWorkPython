# 34.	Подсчитать сумму цифр в вещественном числе.
print('34.	Подсчитать сумму цифр в вещественном числе.')
number = input('Enter the number : ')
result = 0
for i in range(len(number)):
    if number[i].isdigit():
        result += int(number[i])
print(result)
