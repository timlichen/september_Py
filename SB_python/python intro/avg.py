def avg(a):
	sum = 0
	for i in a:
		sum += i
	avg = sum/len(a)
	print avg
avg([1, 2, 5, 10, 255, 3])