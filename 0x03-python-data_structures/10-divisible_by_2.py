#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    another_list = []
    for x in my_list:
        if x % 2 == 0:
            another_list.append(True)
        else:
            another_list.append(False)
    return another_list
