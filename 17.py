letter_conversions = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety"),
    100: len("onehundred"),
    200: len("twohundred"),
    300: len("threehundred"),
    400: len("fourhundred"),
    500: len("fivehundred"),
    600: len("sixhundred"),
    700: len("sevenhundred"),
    800: len("eighthundred"),
    900: len("ninehundred"),
    1000: len("onethousand")
}

summation = 0
for i in range(1, 1001):
    if i <= 20:
        summation = summation + letter_conversions[i]
    elif i <= 99:
        summation = summation + letter_conversions[i%10]
        summation = summation + letter_conversions[int(str(int(i/10)) + "0")]
    elif i <= 999:
        if 10 < int(str(int(i / 10) % 10) + str(i%10)) < 20:
            summation = summation + letter_conversions[int(str(int(i/10)%10) + str(i%10))]
        else:
            summation = summation + letter_conversions[i%10]
            summation = summation + letter_conversions[int(str(int(i/10)%10) + "0")]
        summation = summation + letter_conversions[int(str(int(i/100)) + "0" + "0")]
        if not(i == 100 or i == 200 or i == 300 or i == 400 or i == 500 or i == 600 or i == 700 or i == 800 or i == 900):
            summation = summation + 3
    else:
        summation = summation + letter_conversions[i]
print(summation)
