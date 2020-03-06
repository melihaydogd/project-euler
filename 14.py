def next_step(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return number * 3 + 1


maximum = 0
for i in range(1000000, 500000, -1):
    count = 1
    result = i
    while not result == 1:
        result = next_step(result)
        count += 1
    if count > maximum:
        maximum = count
        num = i
print(num)
