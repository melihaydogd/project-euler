def self_power(number):
    return number**number

summation = 0
for i in range(1, 1001):
    summation = summation + self_power(i)

the_number = ""
num = str(summation)
for i in range(len(num)-10, len(num)):
    the_number = the_number + num[i]

print(the_number)