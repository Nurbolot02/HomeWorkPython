# показать четные числа от 1 до n
n = int(input('Enter the number: '))
for i in range(1, n+1):
    if i %2 == 0:
        print(i, end=' ')
print()