sum = 0

for num in range(2,2000000):
	for i in range(2, num//2):
		if(num % i) == 0:
			break
	else:
		print(num)
		sum = sum + num

print(sum-4)