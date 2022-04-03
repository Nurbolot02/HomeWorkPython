# 31.	Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
import random

print('31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д')
n = int(input('Enter the number: '))
lot_of_n = set()
for i in range(n):
    lot_of_n.add(random.randrange(-999,999))
print(lot_of_n)