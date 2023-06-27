#!i/usr/bin/python3
""" create a class square """


class Square:
    """ represent the class square """

    def __init__(self, size=0):
        """ initialize class square

        Args:
            size: the size of the class square

        Raises:
            typeerror: if the size is not int

            valueerror: if the size is less than zero
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """ return the current area of class square """
        return self.__size * self.__size


    @property
    def size(self):
        """ get the current size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the current value of size """
        if type(value) is not int:

            raise TypeError('size must be an integer')

        if value < 0:

            raise ValueError('size must be >= 0')

        self.__size = value
