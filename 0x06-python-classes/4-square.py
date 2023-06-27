#!/usr/bin/python3
""" define the class square """


class Square:
    """ represnt the class square """

    def __init__(self, size=0):
        """ initialize the class square

        Args:
            size: check if size is not int or not and biggrt than 0 or not
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """ get the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size value """
        if type(value) is not int:
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ func to locate the size area """
        return self.__size ** 2
