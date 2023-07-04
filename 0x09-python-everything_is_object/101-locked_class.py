#!/usr/bin/python3
""" define the class LockedClass """


class LockedClass:
    """
    prevent the user from creating new clacc
    """

    __slots__ = ["first_name"]
