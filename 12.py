def find_divisor_count(number):
    mul = 1
    i = 2
    while number != 1:
        a = 0
        while number % i == 0:
            number = int(number/i)
            a += 1
        mul = mul * (a + 1)
        i += 1
    return mul


count = 0
result = 0
i = 1
while count < 500:
    result = result + i
    count = find_divisor_count(result)
    i += 1

print(result)