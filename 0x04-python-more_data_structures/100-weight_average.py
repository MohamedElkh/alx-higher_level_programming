#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    vg = 0
    value = 0

    for tu in my_list:
        vg += (tu[0] * tu[1])
        value += tu[1]

    return (vg / value)
