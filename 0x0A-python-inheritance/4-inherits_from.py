#!/usr/bin/python3
""" define inherited class """


def inherits_from(obj, a_class):
    """ Checks if an object

    args:
        obj: the object
        a_class: the class to match
    return:
        if obj is an inherited instance
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
