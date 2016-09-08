import random
import time

def insertionsort(a):
	temp = 0
	index = -1
	before = time.time()
	for i in range(1, len(a)):
		temp = a[i]
		index = i

		while index > 0 and a[index-1] > temp:
			a[index] = a[index - 1]
			index = index - 1

		a[index] = temp

	print a
	print time.time() - before

	#0.6 milliseconds

def makelist():
	a = []
	for i in range(0, 100):
		a.append(int(random.random() * 10000))
	return a

insertionsort(makelist())