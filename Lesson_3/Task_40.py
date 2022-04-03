# 40.	Определить, присутствует ли в заданном списке строк, некоторое число
print('40.	Определить, присутствует ли в заданном списке строк, некоторое число ')
userInput = input('Enter the any text: ').split()
print(userInput)
number = int(input('Enter the numer: '))
for i in userInput:
    if i.isdigit() and int(i) == number:
        print(True)
