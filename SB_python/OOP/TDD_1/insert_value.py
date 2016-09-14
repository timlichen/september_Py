def insert_val_at(index, my_list, value):
	if index >= len(my_list):
		return False
	else:
		my_list.insert(index, value)
	return my_list
