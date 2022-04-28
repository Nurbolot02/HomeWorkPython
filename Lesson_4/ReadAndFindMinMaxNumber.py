# 1. Считать строку чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
import random

path = 'numbers.txt'
RA = 'a'
countOfNumbers = 10
numbersList = []

with open(path, RA) as data:
    for i in range(countOfNumbers):
        data.write(str(random.randint(0,100)))
        data.write(' ')
    data.write('\n')

with open(path, 'r') as data:
    s = data.read().split()
    for i in s:
        numbersList.append(int(i))

max = max(numbersList)
min = min(numbersList)
print(f'min = {min} \nmax = {max}')