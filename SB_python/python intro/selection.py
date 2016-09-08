import random
import time

# Completed in 1 millisecond
# Completed in 12 milliseconds
# Completed in 20 milliseconds or 16 milliseconds or 12

def selectionsort(a):
	x = 0
	minindex = 0
	maxindex = 0
	print a
	before = int(round(time.time() * 1000))

	while x < len(a):

		mindone = False
		maxdone = False
		maximum = a[len(a) - 1 - x]
		minimum = a[x]

		count = 0

		for i in range(x, len(a)):

			if a[i] < a[x] and minimum > a[i]:

				minimum = a[i]
				minindex = i
				mindone = True

			if a[len(a) - 1 - i] > a[len(a) - 1 - x] and maximum < a[len(a) - 1 - i]:

				maximum = a[len(a) - 1 - i]
				maxindex = len(a) - 1 - i
				maxdone = True

		if minimum < a[x] and mindone:

			a[minindex] = a[x]
			a[x] = minimum

		if maximum > a[len(a) - 1 - x] and maxdone:

			a[maxindex] = a[len(a) - 1 - x]
			a[len(a) - 1 - x] = maximum

		print a
		x += 1

	print a
	print "Completed in", int(round(time.time() * 1000)) - before, "millisecond(s)"

def makelist():
	a = []
	for i in range(0, 100):
		a.append(int(random.random() * 10000))
	return a

selectionsort(makelist())