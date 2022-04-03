# Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1
n = int(input('Enter the number: '))
dict = {}
for k in range(1, n+1):
    dict[k] = 3 * k +1
print(dict)