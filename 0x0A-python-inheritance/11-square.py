#!/usr/bin/python3
""" deifne the rect """
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ represnt a square """

    def __init__(self, size):
        """ initialize a square

        args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
