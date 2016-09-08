max = 0
print max

def maxminavg(a):
	max = a[0]
	min = a[0]
	sum = 0
	for e in a:
		if e < min:
			min = e
		if e > max:
			max = e
		sum += e
	avg = sum / len(a)
	print max, min, avg

maxminavg([0,1,2,3,4])