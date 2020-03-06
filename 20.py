def fac(number):
    if number == 0:
        return 1
    else:
        return number*fac(number-1)

summation = 0
number = str(fac(100))
for i in range(0, len(number)):
    summation = summation + int(number[i])
print(summation)
