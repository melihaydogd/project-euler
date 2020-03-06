def find_fifth_power(number):
    return number**5


def find_sum_of_fifth_powers(number):
    string = str(number)
    result = 0
    for i in range(len(string)):
        result = result + find_fifth_power(int(string[i]))
    return result

result = 0
for i in range(2, 1000000):
    if i == find_sum_of_fifth_powers(i):
        print(i)
        result = result + i

print(result)