def print_1_255():
	for x in range(1, 256):
		print x

def print_odd_1_255():
	for x in range(1, 129):
		print 2*x -1

def print_int_sum():
	intsum = 0
	for x in range(1, 256):
		intsum += x
		print "int: " + str(x) + " sum: " + str(intsum)

def print_array(arr):
	for x in range(0, len(arr)):
		print arr[x]

def find_max(arr):
	print max(arr)

def print_ave(arr):
	print float(sum(arr)) / len(arr)

def array_odds():
	arr = []
	for x in range(1, 256, 2):
		arr.append(x)
	return arr

def square_val(arr):
	for x in range(0, len(arr)):
		arr[x] *= arr[x]
	return arr

def greater_than_Y(arr, y):
	count = 0
	for x in range(0, len(arr)):
		if arr[x] > y:
			count += 1
	print count

def zero_negetive(arr):
	for x in range(0,len(arr)):
		if5 arr[x] < 0:
			arr[x] = 0
	return arr

def max_min_ave(arr):
	print "Max: " + str(max(arr)) + " Min: " + str(min(arr)) + " Ave: " + str(float(sum(arr)) / len(arr))

def shift_array(arr):
	for x in range(0, len(arr)-1):
		arr[x] = arr[x+1]
	arr[len(arr)-1] = 0
	return arr

def swap_negative(arr):
	for x in range(0, len(arr)):
		if arr[x] < 0:
			arr[x] = "Dojo"
	return arr