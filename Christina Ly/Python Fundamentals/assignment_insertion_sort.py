import random
def makesample():
	a = []
	for e in range(1,101):
		a.append(random.randint(0,10000))
	return a

def insertionsort(a):
	for i,e in enumerate(a):
		ind = i
		for k in range(i,-1,-1):
			if a[i] < a[k]:
				ind = k
		val = a.pop(i)
		a.insert(ind, val)
	print a
insertionsort(makesample())