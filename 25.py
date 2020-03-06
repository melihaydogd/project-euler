def find_digit_number(num):
    return len(str(num))


def next_step(arr):
    length = len(arr)
    return arr[length - 1] + arr[length - 2]


fib_array = [1, 1]
while not find_digit_number(fib_array[len(fib_array) - 1]) == 1000:
    fib_array.append(next_step(fib_array))
print(len(fib_array))

