#!/usr/bin/python3
""" define the func say_my_name """


def say_my_name(first_name, last_name=""):
    """ func to print my name

    Args:
        first_name: name to be printed
        last_name: last name to be printed
    Raise:
        typeerror: it first and last are not string
    """

    if not isinstance(first_name, str):

        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):

        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
