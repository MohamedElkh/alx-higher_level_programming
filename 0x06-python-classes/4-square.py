#!i/usr/bin/python3
""" create a class square """


class Square:
    """ represent the class square """

    def __init__(self, size=0):
        """ initialize class square

        Args:
            size: the size of the class square
        """

        self.size = size

    @property
    def size(self):
        """ get the current size of the square """

        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the current size of the square """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ return the current area of class square """

        return self.__size ** 2
