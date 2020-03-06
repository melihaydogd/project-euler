a = 2
count = 1
while count != 501:
	
	for i in range(1,a):
		sum = int((a * (a-1)) / 2)
	else:
		for j in range(1,int(sum/2)+1):
			if(sum % j == 0):
				count = count + 1
		else:
			print(count)
			if(count == 501):
				print(sum)
			count = 1
	a = a + 1
