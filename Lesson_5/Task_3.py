# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = "Напишитеабв программу, удаляющую изабв текста все слова, содержащие".split()
print(text)
result = ''

for i in text:
    if i.find('абв') == -1:
        result += i + ' '
print(result)

result2 = [i for i in text if i.find('абв') == -1]
print(result2)