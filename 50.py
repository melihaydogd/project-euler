def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num/2), 2):
        if num % i == 0:
            return False
    return True


def sum_of_primes(primes, exception):
    maximum = 0
    index = 0
    result = 0
    count = 0
    cc = 0
    for i in range(exception, len(primes)):
        result = result + primes[i]
        count += 1
        if result >= 1000000:
            break
        if is_prime(result):
            maximum = result
            cc = count
    arr = [maximum, cc]
    return arr

prime_numbers = [2, 3]
summation = 5
prime = True
i = 5
while i < 2500:
    for j in range(len(prime_numbers)):
        if i % prime_numbers[j] == 0:
            prime = False
    if prime:
        summation = summation + i
        prime_numbers.append(i)
    prime = True
    i += 1

i = 0
max_value = 0
maximum = 0
while i < 1000:
    if is_prime(sum_of_primes(prime_numbers, i)[0]):
        if sum_of_primes(prime_numbers, i)[1] > maximum:
            maximum = sum_of_primes(prime_numbers, i)[1]
            max_value = sum_of_primes(prime_numbers, i)[0]
    i += 1
print(maximum)
print(max_value)

