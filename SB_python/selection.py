import random
import time

def selectionsort(a):
	x = 0
	index = 0
	print a
	before = int(round(time.time() * 1000))
	while x < len(a) - 1:
		done = False
		minimum = a[x]
		for i in range(x, len(a)):
			if a[i] < a[x] and minimum > a[i]:
				minimum = a[i]
				index = i
				done = True
		if minimum < a[x] and done:
			a[index] = a[x]
			a[x] = minimum
		x += 1
	print a
	print "Completed in", int(round(time.time() * 1000)) - before, "millisecond(s)"

def makelist():
	a = []
	for i in range(0, 100):
		a.append(int(random.random() * 10000))
	return a

selectionsort(makelist())