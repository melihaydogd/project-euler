for c in range(3,1000):
	for b in range(2,c):
		for a in range(1,b):
			if((a*a + b*b == c*c) & (a + b + c == 1000)):
				print(a,b,c)
				print(a*b*c)
		
	