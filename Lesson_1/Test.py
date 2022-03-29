print("HI")
numbers = [1,0,0,1,0,1,1,0,0,0,1]
for i in numbers:
    if i == 1:
        i
    else:
        numbers[i] = 1
    print(i)
