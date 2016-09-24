

def bubbleSort():
	arr = [7,3,4,1,9,3,5]
	temp = 0
	count = 0
	for x in range(0, len(arr) - 1):

		temp = arr[x]  # set temp to arr x 
		if (arr[x] > arr[x+1]):
			arr[x] = arr[x+1]
			arr[x+1] = temp
		
	print arr

bubbleSort()

# 7 is greater than 3, so swap them [3,7,4,1,9,3,5] 1st loop
# 7 is greater than 4, so swap them [3,4,7,1,9,3,5] 1st loop
# 7 is greater than 1, so swap them [3,4,1,7,9,3,5] 1st loop 
# 7 is less than 9, so start over [3,4,1,7,9,3,5] 
# 3 is less than 9, so swap [3,4,1,7,3,9,5]
# 7 is less than 9, so keep going [3,4,1,7,3,5,9]


		# compare arr x to arrx + 1
		# set arr x to arr x + 1 if arr x > 
