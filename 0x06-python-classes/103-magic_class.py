#!/usr/bin/python3
""" define magic class and use the math """


import math
""" define the magicclass """


class MagicClass:
    """ represent the class magic """

    def __init__(self, radius=0):
        """ initialize the magicclass

        Args:
           radius: check if it not int and not float
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:

            raise TypeError("radius must be a number")

        self.__radius = radius

    def circumference(self):
        """ func to return the value of magicclass """
        return (2 * math.pi * self.__radius)

    def area(self):
        """ func to return the area of magicclass """
        return (self.__radius ** 2 * math.pi)
