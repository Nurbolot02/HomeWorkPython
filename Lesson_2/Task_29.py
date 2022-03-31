# Показать кубы чисел, заканчивающихся на четную цифру
print('Показать кубы чисел, заканчивающихся на четную цифру')
number = int(input('Enter the number: '))
i = 1
degree = 3
while number >= i:
    print(i ** 3, end= ' ')
    i += 1