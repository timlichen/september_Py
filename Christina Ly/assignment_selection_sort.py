import random
def makesample():
	a = []
	for e in range(0,101):
		a.append(random.randint(0,10000))
	return a
def selectionsort(a):
	for i,e in enumerate(a):
		min = a[i]
		ind = i
		for k in range(i, len(a)):
			if a[k] < min:
				min = a[k]
				ind = k
		(a[i], a[ind]) = (a[ind], a[i])
	print a
selectionsort(makesample())

def selectionsort2(a):
	for i in range(0,len(a)/2):
		min = a[i]
		max = a[i]
		mini = i
		maxi = i
		for k in range(i,len(a)-i):
			if a[k] < min:
				min = a[k]
				mini = k
			elif a[k] > max:
				max = a[k]
				maxi = k
		(a[mini], a[i]) = (a[i], a[mini])
		if maxi != i:
			(a[len(a)-1-i], a[maxi]) = (a[maxi], a[len(a)-1-i])
	print a
selectionsort2(makesample())