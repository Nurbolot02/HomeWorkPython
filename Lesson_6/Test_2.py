# filte lambda
age_List = [32, 8, 45, 17, 25]
print(age_List)
age_List = set(filter(lambda age: age > 16, age_List))
print(age_List)