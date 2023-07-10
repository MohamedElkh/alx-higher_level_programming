#!/usr/bin/python3
""" define the function adds attrs """


def add_attribute(obj, at, value):
    """ add new attribute

    args:
        obj: the object
        at: the name of attribute
        value: the value
    raise:
        typeerror: if attribute can not be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, at, value)
