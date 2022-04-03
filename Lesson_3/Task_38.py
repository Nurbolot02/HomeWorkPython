# 38.	Реализовать алгоритм перемешивания списка.
print('38.	Реализовать алгоритм перемешивания списка. ')

def list_shuffling(lst):
    length = len(lst)
    for i in range(0, length // 2):
        buffer = lst[i]
        lst[i] = lst[length - 1 - i]
        lst[length - 1 - i] = buffer

lst = [1,5,9,6,64,6,5]
print(lst)
list_shuffling(lst)
print(lst)