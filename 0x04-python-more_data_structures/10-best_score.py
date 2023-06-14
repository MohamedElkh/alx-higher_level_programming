#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    mx_dic = max(a_dictionary.values(), default=None)
    
    for x, z in a_dictionary.items():
        if z == mx_dic:
            return x	
