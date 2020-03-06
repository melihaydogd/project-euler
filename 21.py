def sum_of_proper_divisors(number):
    result = 0
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            result = result + i
    return result

summation = 0
for i in range(1, 10000):
    if i == sum_of_proper_divisors(sum_of_proper_divisors(i)) and not i == sum_of_proper_divisors(i):
        summation = summation + i

print(summation)


