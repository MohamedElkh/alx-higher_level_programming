#!/usr/bin/python3
""" define the interger addition """


def add_integer(a, b=98):
    """ return the addition between a and b
    Raises:
        typeerror: it a and b not int and float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):

        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):

        raise TypeError("b must be an integer")

    return (int(a) + int(b))
