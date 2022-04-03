def toBinary(number):
    result = []
    while number > 0:
        result.insert(0, number % 2)
        number //= 2
    return result