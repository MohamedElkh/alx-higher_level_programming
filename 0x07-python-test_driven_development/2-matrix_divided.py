#!/usr/bin/python3
""" define a function matrix division """


def matrix_divided(matrix, div):
    """ function to divide all elem in the matrix
    Args:
        matrix: is a list of lists of int and floats
        div: the character to be checked
    Raises:
        typeerror: if the matrix not a number or not int or float
    Return:
        a new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(el, int) or isinstance(el, float))
                    for el in [n for r in matrix for n in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):

        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):

        raise TypeError("div must be a number")

    if div == 0:

        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda i: round(i / div, 2), r)) for r in matrix])
