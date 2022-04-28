# 51.	Составить список простых множителей натурального числа N

from useFulFutires.Factor import factor
from useFulFutires.IsNumber import isNumber

print('51.	Составить список простых множителей натурального числа N')
nuberString = 'Enter the N: '
number = isNumber(nuberString)
result = factor(number)
print(result)
