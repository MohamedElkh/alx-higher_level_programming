#!/usr/bin/python3
"""define a Rectangle class."""


class Rectangle:
    """Represent rectangle.

    Attribute:
        number_of_instances : the number of Rectangle instances.
        print_symbol : the symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle.

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
        """ set the value of class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
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
        """Return representation of the Rectangle."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"

        return (r)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1

        print("Bye rectangle...")
