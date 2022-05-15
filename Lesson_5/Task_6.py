# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def Zipper(readingData):
    buffer = ''
    counter = 0
    RLEList = []
    dataLength = len(readingData)
    for i in range(dataLength):
        if buffer == '':
            buffer = readingData[i]
            counter = 1
        elif readingData[i] == buffer:
            if i == dataLength - 1:
                counter += 1
                RLEList.append((buffer, counter))
            else:
                counter += 1
        else:
            RLEList.append((buffer, counter))
            buffer = readingData[i]
            counter = 1
    return RLEList

def UnZipper(RLEList):
    result = ''
    for i in RLEList:
        result += f'{i[0]}' * i[1]
    return result


path = 'Task_6.txt'
with open(path, 'r') as data:
    readingData = data.read()
RLEResult = Zipper(readingData)
print(RLEResult)
UnZipperResult = UnZipper(RLEResult)
print(UnZipperResult)
pathZippingFile = 'Task_6_ZippingFile'
with open(pathZippingFile, 'w') as data:
    data.write(f'{RLEResult}')

