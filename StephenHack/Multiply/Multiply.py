def mult(arr, i):
	# i = 5
	# arr = [2,4,10,16]
	newarr = [];
	for x in range(0, len(arr)):
		newarr.append(arr[x]*i)  
	print newarr


mult([2,4,10,16], 5)

