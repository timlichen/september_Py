import random
def createsample():
	a = []
	for e in range(0,101):
		a.append(random.randint(0,10000))
	return a

def bubblesort(a):
	for index, e in enumerate(a):
		for k in range(0,len(a)-1-index):
			if a[k] > a[k+1]:
				(a[k], a[k+1]) = (a[k+1], a[k])
	print a
bubblesort(createsample())

