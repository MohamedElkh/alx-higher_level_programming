#!/usr/bin/python3
""" define a class """


def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance

    args:
        obj: the object
        a_class: the class to match
    return:
        if obj is an instance
    """

    if isinstance(obj, a_class):
        return True
    return False
