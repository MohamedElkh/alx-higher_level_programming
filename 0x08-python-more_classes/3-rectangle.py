#!/usr/bin/python3
""" define the class rectange """


class Rectangle:
    """ represtent the class """

    def __init__(self, width=0, height=0):
        """ inittialize the class
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
        """ set the value of the width """
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
        """ return the pre of class """
        if self.__width == 0 or slef.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ return the printable string """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []

        for x in range(self.__height):
            [r.append('#') for a in range(self.__width)]

            if x != self.__height - 1:
                r.append("\n")

            return ("".join(r))
