def secondToLast(arr):
	if len(arr) < 2:
		return 0
	else:
		return arr[len(arr) - 2]

print secondToLast([0,1,2,3])

def nthtolast(arr, i):
	if len(arr) < i:
		return 0
	else:
		return arr[len(arr) - i]

print nthtolast([0,1,2,3], 3)

def secondLargest(arr):
	if len(arr) < 2:
		return 0
	else:
		i = 0
		for i in range(0, len(arr) - 1):
			if arr[i] < arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				i = -1
		print arr
		return arr[1]

print secondLargest([0,1,2,3,4,5,6])