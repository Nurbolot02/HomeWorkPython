# 37.	Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число
import random

print('37.	Задать список из N элементов, заполненных числами из [-N, N]. '
      'Найти произведение элементов на указанных позициях. '
      'Позиции хранятся в файле file.txt в одной строке одно число')
flag = True
while flag:
    n = input('Enter the number: ')
    if n.isdigit():
        n = int(n)
        while True:
            if n >= 6:
                flag = False
            else:
                print('число должен быть больше 5')
            break
listN = []
for i in range(n):
    listN.append(random.randint(-n, n))

path = 'file.txt'
result = 1

with open(path, 'r') as data:
    for i in data:
        result *= listN[int(i)]
print(result)