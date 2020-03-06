def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num/2), 2):
        if num % i == 0:
            return False
    return True


def find_primes(add_prime):
    find = False
    i = add_prime[len(add_prime)-1]
    while not find:
        i += 1
        for j in add_prime:
            if i % j == 0:
                find = False
                break
            else:
                find = True
    return i

prime_list = [2]
value = 0
cc = 0
temp_count = 0
count = 1
result = 2
maximum = 0
while result < 1000000:
    if result > maximum:
        temp_count = count
        maximum = result
        i = 0
        while not is_prime(maximum) and maximum > 0:
            # deletes and reduces
            maximum = maximum - prime_list[i]
            temp_count -= 1
            i += 1
    result = result + find_primes(prime_list)
    prime_list.append(find_primes(prime_list))
    count += 1
    if is_prime(result):
        value = result
        cc = count

print(cc)
print(value)
print(temp_count)
print(maximum)


