def draw_stars(my_list):
	for i in range(0, len(my_list)):
		if type(my_list[i]) is int:
			print "*" * my_list[i]
		elif type(my_list[i]) is str:
			my_string = my_list[i].lower()
			char = my_string[0]
			print char*len(my_string)