# Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = "Напишитеабв программу, удаляющую изабв текста все слова, содержащие".split()
textResult = list(filter(lambda t: t.find('абв') == -1, text))
print(textResult)