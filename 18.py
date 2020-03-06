number_file = open("18.txt", "r")
numbers = number_file.read().split("\n")
for i in range(len(numbers)):
    numbers[i] = numbers[i].split(" ")
i = len(numbers) - 1
while i != 0:
    j = 0
    while j != i:
        temp = int(numbers[i - 1][j]) + int(numbers[i][j])
        temp1 = int(numbers[i - 1][j]) + int(numbers[i][j + 1])
        if temp > temp1:
            numbers[i - 1][j] = temp
        else:
            numbers[i - 1][j] = temp1
        j += 1
    i -= 1
print(numbers)