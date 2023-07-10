#!/usr/bin/python3
""" define the rect """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represent the class """

    def __init__(self, size):
        """ intialize the func

        args:
            size: size of new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
