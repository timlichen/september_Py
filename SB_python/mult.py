def fives():
	for i in range(5, 1000000):
		if (i%5 == 0):
			print i

def odds():
	for i in range(1, 1000):
		if (i%2 != 0):
			print i
odds()
fives()