num = str(2**1000)

summation = 0
for i in range(len(num)):
    summation = summation + int(num[i])
print(summation)