#!/usr/bin/python3
""" define the class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represent the class """

    def __int__(self, width, height):
        """ initia;ize the func

        args:
            width: the width of rect
            height: the hieght of rect
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self._width = width
        self._height = height
