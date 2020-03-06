alphabet = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}
name_file = open("22.txt", "r")
names = sorted(name_file.read().replace('"',"").split(','))
name_file.close()

summation = 0
for i in range(len(names)):
    char_sum = 0
    for j in range(len(names[i])):
        char_sum = char_sum + alphabet[names[i][j]]
    multiple = char_sum * (i+1)
    summation = summation + multiple
print(summation)











# name = ""
# if "a" > "z":
#     name = name + "a"
# else:
#     name = name + "b"
# print(name)bb

# name_array = [[]]
# name_array[0].insert(0, "a")
# name_array[0].insert(1, "h")
# print(name_array[0][1])



