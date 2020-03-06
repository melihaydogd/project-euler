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

prime_arr = [2]
divisor = []
power = []
result = 0
i = 1
mul = 0
while mul < 50:
    mul = 1
    result = result + i
    while find_primes(prime_arr) < result:
        prime_arr.append(find_primes(prime_arr))
    for j in prime_arr:
        if result % j == 0:
            divisor.append(j)
    b = 0
    for j in divisor:
        power.append(0)
        a = j
        while result % a == 0:
            power[b] += 1
            a = a * a
        b += 1
    for j in power:
        mul = mul * (j + 1)
    i += 1
    print(mul)
    divisor.clear()
    power.clear()

print(result)
