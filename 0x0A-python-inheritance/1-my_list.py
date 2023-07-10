#!/usr/bin/python3
""" define the inherted list """


class MyList(list):
    """ represent the class """

    def print_sorted(self):
        """ print a list in order """
        print(sorted(self))
