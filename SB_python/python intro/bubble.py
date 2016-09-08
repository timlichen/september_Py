import random
import time

def bubblesort(a):
	check = -1
	done = False
	test = []
	before = int(round(time.time()* 1000))
	while check == -1 or check > 0:
		for i in range(0, len(a)):
			if i < len(a) - 1:
				one, two = (a[i], a[i+1])
				if one > two:
					(a[i], a[i+1]) = (a[i+1], a[i])
			if i == len(a) - 1 and a[i] == max(a) and not done:
				check = i
				done = True
			if i == check - 1:
				check = i
	print a
	print 'This took', int(round(time.time() * 1000)) - before, 'milliseconds to complete'

def makelist():
	a = []
	for i in range(0, 100):
		a.append(int(random.random() * 10000))
	return a

bubblesort(makelist())