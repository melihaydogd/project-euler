result = 0
count = -1
i = 1
increment = 2
while i <= 1001*1001:
    result = result + i
    count += 1
    if count % 4 == 0 and not count == 0:
        increment += 2
    i += increment
print(result)