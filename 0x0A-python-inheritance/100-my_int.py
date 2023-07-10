#!/usr/bin/python3
""" define the class """


class MyInt(int):
    """ represnt the class """

    def __eq__(self, value):
        """ function to override """
        return self.real != value

    def __ne__(self, value):
        """ func to over ride """
        return self.real == value
