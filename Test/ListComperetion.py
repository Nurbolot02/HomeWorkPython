from useFulFutires.IsNumber import isNumber

number  = isNumber()
list = [ [i, i ** 2] for i in range(number) if i % 2 != 0]
print(list)