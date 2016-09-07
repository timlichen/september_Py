import random
the_list = []
for i in range(0, 100):
	the_list.append(int(random.random()*10000))
def selec_sort(my_list):
	count = 0
	while count < len(my_list) -1:
		m = count
		for i in range(count, len(my_list)-1):
			if my_list[m] > my_list[i+1]:
				m = i+1
		my_list[count], my_list[m] = my_list[m], my_list[count]
		count += 1
	return my_list

def selec_sortv2(my_list):
	count = 0
	while count < len(my_list)/2:
		mindex = count
		maxdex = len(my_list)-1-count
		for i in range(count, len(my_list)-1-count):
			if my_list[mindex] > my_list[i+1]:
				mindex = i+1
			if my_list[maxdex] < my_list[i]:
				maxdex = i
		my_list[len(my_list)-1-count], my_list[maxdex] = my_list[maxdex], my_list[len(my_list)-1-count]
		my_list[count], my_list[mindex] = my_list[mindex], my_list[count]
		count += 1
	return my_list
print selec_sort(the_list)
print selec_sortv2(the_list)