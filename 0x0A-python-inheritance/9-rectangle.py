#!/usr/bin/python3
""" define the class rect """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represnt the class """
    def __int__(self, width, height):
        """ intialize the rect

        args:
            width: the width of rect
            height: the height of rect
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return the area of rect """
        return self.__width * self.__height

    def __str__(self):
        """ return the print and str """
        stri = "[" + str(self.__class__.__name__) + "] "
        stri += str(self.__width) + "/" + str(self.__height)
        return stri
