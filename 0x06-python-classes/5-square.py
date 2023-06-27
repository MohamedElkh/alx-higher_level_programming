#!/usr/bin/python3
""" define the class square """


class Square:
    """ represent the class square """

    def __init__(self, size=0):
        """ initialize the class square

        Args:
            size: the size of the class square

        Define:
            if the size in int or not or less than zero
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """ get the size of the square """
        return self.__size

    @size.setter
    def size(self, size):

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ func to return the current square """
        return self.__size ** 2

    def my_print(self):
        """ func to print the hash character """
        if self.__size == 0:
            print()
            return None

        for x in range(1, self.area() + 1):
            print('#', end='')

            if x % self.__size == 0 and x > 0:
                print()
