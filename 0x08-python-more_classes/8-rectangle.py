#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Represent rectangle.

    Attribute:
        number_of_instances : The number of Rectangle instances.
        print_symbol : The symbol used for string representation.
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width : The width of the new rectangle.
            height : The height of the new rectangle.
        """
        type(self).number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get height of the Rectangle."""
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
        """Return area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 : The first Rectangle.
            rect_2 : The second Rectangle.

        Raises:
            TypeError: if either of rect_1 or rect_2 is not a Rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for x in range(self.__height):
            [r.append(str(self.print_symbol)) for a in range(self.__width)]

            if x != self.__height - 1:
                r.append("\n")

        return ("".join(r))

    def __repr__(self):
        """Return the str representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"

        return (r)

    def __del__(self):
        """Print message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1

        print("Bye rectangle...")
