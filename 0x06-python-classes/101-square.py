#!/usr/bin/python3
""" define the class square """


class Square:
    """ represent the class square """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size

        self.position = position

    @property
    def size(self):
        """ get the current value """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the current value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ get the current value of the position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ set the current value of the position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ function to define the area of self """
        return (self.__size * self.__size)

    def my_print(self):
        """ func to print white space """
        if self.__size == 0:

            print("")
            return

        [print("") for x in range(self.__position[1])]

        for x in range(self.__size):

            [print(" ", end="") for i in range(self.__position[0])]

            [print("#", end="") for a in range(self.__size)]
            print("")

    def __str__(self):
        """ func to print the value """
        if self.__size != 0:

            [print("") for x in range(self.__position[1])]

        for x in range(self.__size):

            [print(" ", end="") for d in range(self.__position[0])]

            [print("#", end="") for f in range(self.__size)]

            if x != self.__size - 1:

                print("")

        return ("")
