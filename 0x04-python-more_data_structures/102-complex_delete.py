#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for x, g in a_dictionary.items():
            if g == value:
                del a_dictionary[x]
                break

    return (a_dictionary)
