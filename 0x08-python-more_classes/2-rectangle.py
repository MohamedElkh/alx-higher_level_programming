#!/usr/bin/python3
""" define a class rectange """


class Rectangle:
    """ represtent the class """

    def __init__(self, width=0, height=0):
        """ initialize a rectange

        args:
            width : the width of the new rectangle.
            height : the height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the value of width """
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

    def area(self):
        """ return the area of the class """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return the per of the class """
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))
