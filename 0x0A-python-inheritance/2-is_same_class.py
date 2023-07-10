#!/usr/bin/python3
""" define a class checking """


def is_same_class(obj, a_class):
    """ check the object

    args:
        obj: the object to be checked
        a_class: the class to match the type
    return:
        if obj is instance
    """

    if type(obj) == a_class:
        return True

    return False
