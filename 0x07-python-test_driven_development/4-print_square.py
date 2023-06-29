#!/usr/bin/python3
""" define the func print_square """


def print_square(size):
    """ func to print the character #
    Args:
        size: the height and width of the square
    Raises:
        typeerror: if the size not int
        valueerror: if size < 0
    """

    if not isinstance(size, int):

        raise TypeError("size must be an integer")

    if size < 0:

        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for i in range(size)]

        print("")
