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
	avg = sum/len(a)
	print min, max, avg
maxminavg([1,2,3,4])