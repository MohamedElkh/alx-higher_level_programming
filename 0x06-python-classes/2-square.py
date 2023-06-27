#!/usr/bin/python3
""" define the class square """


class Square:
    """ the class square """

    def __init__(self, size=0):
        """
        create a function for the class square

        Args:
            size: the size of the square
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
