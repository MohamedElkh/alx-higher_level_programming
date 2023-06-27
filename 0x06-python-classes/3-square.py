#!/usr/bin/python3
""" create a class square """


class Square:
    """ class square """
    def __init__(self, size=0):
        """ create a function for the new square

        Args:
            size: the size of the class square
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ function to return the current area of the square """

        return self.__size ** 2
