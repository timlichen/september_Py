import random
def bubble_sort(my_list):
	count = 1
	while count < len(my_list):
		for i in range(0, len(my_list)-1):
			if my_list[i] > my_list[i+1]:
				my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
		count += 1
	return my_list

the_list = []
for i in range(0, 100):
	the_list.append(round(random.random()*10000))
print bubble_sort(the_list)