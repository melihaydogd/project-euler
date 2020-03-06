months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

count = 0
sunday = 6
month = 1
for i in range(1, 101):
    month = 1
    while month <= 12:
        days = months[month]
        if i % 4 == 0 and month == 2:
            days += 1
        while sunday <= days:
            if sunday == 1:
                count += 1
            sunday += 7
        sunday = sunday % days
        month += 1
print(count)