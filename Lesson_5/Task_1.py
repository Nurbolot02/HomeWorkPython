## 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5
txt = '1 2 4 5 '
path = 'task_1.txt'
with open(path, 'w') as f:
    f.write(txt)
with open(path, 'r') as f:
    txt = f.read().split()
numbers = [int(txt[i]) - 1 for i in range(len(txt)) if (int(txt[i]) - 1) != int(txt[i-1])]
print(numbers)