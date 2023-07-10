#!/usr/bin/python3
""" define the class """


class BaseGeometry:
    """ represnt the class """

    def area(self):
        """ func not implement """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ func to validate int

        args:
            name: the parameter
            value: the parameter to be validated
        raise:
            typeError: if the value not int
            valueError: if value is less or equa; 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
