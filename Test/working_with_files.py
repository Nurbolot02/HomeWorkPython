colors = {'Grean','Blue','Yellow'}
path = 'text.txt'
count = 1
with open(path, 'r+') as file:
    for i in colors:
        file.write(f'{count} ')
        count += 1
        file.write(i)
        file.write('\n')
    s = file.read()
    print(s)
# data = open('text.txt', 'w')
# for i input_data colors:
#     data.write(colors[i])
#     data.write(' ')
# data.close()
# path = 'text.txt'
#
# with open(path,'') as data:
#     for i input_data data:
#         data.write(colors[i])
#         data.write(' ')
#         print(i)
# #
# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string(5))
#
# def continio(*params):
#     res: str = ''
#     for i input_data params:
#         res += i
#     return res
# print(continio('rew ', '558 ', 'erfw ', 'ewrfew '))

# a = [1, 2, 5, 6, 8]
# c = tuple(a)
# print(a)
# print(c)
#
# a[0] = 99
#
# print(a)
# print(c)

# dictionary = \
#     {
#     'up' : '1',
#     'left': '2',
#     'down': '3',
#     'rigth': '4'
# }
# print(dictionary)
# for i input_data dictionary:
#     print(i,' ', dictionary[i])
# print('*-------------------------------------------------------------------------*')
# numbers_1 = {1,2,3,4,5,6}
# numbers_2 = {5,8,46,46,6}
#
# numbersUnion = numbers_1.union(numbers_2)
# print(numbers_1)
# print(numbers_2)
#
# numbersSection = numbers_1.intersection(numbers_2)
# numOneDiffNumTwo = numbers_1.difference(numbers_2)
# numTwoDiffOne = numbers_2.difference(numbers_1)
#
# print(numbersSection)
# print(numOneDiffNumTwo)
# print(numTwoDiffOne)
#
# numbersUnionFrozenSet = frozenset(numbersUnion)
#
# numbers_11 = [1,2,3,4,5,6]
# print(numbers_11)
# numbers_11.pop(2)
# numbers_11.insert(0, 5)
# print(numbers_11)
