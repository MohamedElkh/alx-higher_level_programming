#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
       	return (0)

     vg = 0
     value = 0
     for t in my_list:
         vg += (t[0] * t[1])
	 value += t[1]
     return (vg /value)		
