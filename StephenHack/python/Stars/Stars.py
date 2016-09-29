def draw_stars1(arr):
	for x in range(0, len(arr)):
		print arr[x] * "*"

draw_stars1([3,4,2,3,4])


def draw_stars2(arr):
	for x in arr: 
		if (type(x) == str):
			print x[0] * len(x)
		else:
			print x * "*"

draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])


# a=[1,2,3,4,5]
# for anyelementoranyothername in a:
# 	print anyelementoranyothername