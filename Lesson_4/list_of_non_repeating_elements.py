# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = input('enter a number separated by a space: ').split()
numbers = [int(i) for i in numbers]
nonRepeatingListOfNumbers = []
length = len(numbers)
nonRepeatingListOfNumbers.append(numbers[0])

for i in range(length):
    for j in range(len(nonRepeatingListOfNumbers)):
        if numbers[i] == nonRepeatingListOfNumbers[j]:
            break
        elif j == len(nonRepeatingListOfNumbers) - 1:
            nonRepeatingListOfNumbers.append(numbers[i])
print(f'Основной список: {numbers}')
print(f'Отсортированый с помощю алгоритма: {nonRepeatingListOfNumbers}')

nonRepeatingListOfNumbers2 = list(set(numbers))
print(f'С ипользованием функции Python3: {nonRepeatingListOfNumbers2}')