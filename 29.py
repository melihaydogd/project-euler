def find_power(number, arr):
    for i in range(2, 101):
        value = number**i
        found = False
        for j in range(len(arr)):
            if value == arr[j]:
                found = True
                break
        if not found:
            arr.append(value)

array = []
for i in range(2, 101):
    find_power(i, array)
print(len(array))
