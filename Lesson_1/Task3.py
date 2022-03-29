# по заданному номеру дня недели вывести его название

WeekDays = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
number = int(input('Enter the number: ')) - 1
if number <= 0 or number >= len(WeekDays):
    print("Not")
else:
    print(WeekDays[number])
