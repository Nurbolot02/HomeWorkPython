# Дано число из отрезка [10, 99]. Показать наибольшую цифру
from useFulFutires.IsNumber import isNumber

numText = 'Введите число: '
number = isNumber(numText)

numberList = []
while number > 0:
    numberList.append(number % 10)
    number //= 10

numberListLength = len(numberList)
maxNumber = numberList[0]
minNumber = numberList[0]

for i in range(numberListLength):
    if numberList[i] > maxNumber:
        maxNumber = numberList[i]
    elif numberList[i] < minNumber:
        minNumber = numberList[i]
print(f'maxNumber: {maxNumber}, minNumber: {minNumber}')