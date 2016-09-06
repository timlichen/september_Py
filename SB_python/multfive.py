def multfive(a, x):
	for e in range(0, len(a)):
		a[e] *= x
	print a

multfive([2, 4, 10, 16], 5)