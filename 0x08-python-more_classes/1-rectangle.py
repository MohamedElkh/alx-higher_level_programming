#!/usr/bin/python3
""" define class rectangle """


class Rectangle:
    """ represent the class """

    def __init__(self, width=0, height=0):
        """ initializtion the class

        args:
            width : The width of the new rectangle.
            height : The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the value of size """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
