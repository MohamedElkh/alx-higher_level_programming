#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	new_copy = mylist.copy()

	if idx < 0 or idx >= len(my_list):
		return new_copy
	new_copy[idx] = element
	return new_copy
