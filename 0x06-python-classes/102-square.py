#!/usr/bin/python3
""" define the class square """


class Square:
    """ represent the class square """
    def __init__(self, size=0):
        """ initialize the class square """
        self.size = size

    @property
    def size(self):
        """ get the size value """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the size value """
        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        elif value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ return the current area """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ func to define the comparision """
        return self.area() == other.area()

    def __lt__(self, other):
        """ func to define < comparision """
        return self.area() < other.area()

    def __ne__(self, other):
        """ func define to not comparision """
        return self.area() != other.area()

    def __le__(self, other):
        """ func to define <= comparison """
        return self.area() <= other.area()

    def __ge__(self, other):
        """ func to define >= comparision to square """
        return self.area() >= other.area()

    def __gt__(self, other):
        """ func to define the > comparision """
        return self.area() > other.area()
