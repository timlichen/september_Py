def sumList(arr):
	# arr = [1,2,5,10,255,3]
	sum = 0
	for x in range(0, len(arr)):
		sum += arr[x]
	print sum

sumList([5,10,255,20])