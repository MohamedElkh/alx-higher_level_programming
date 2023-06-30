#!/usr/bin/python3
""" define a matric mult """


def matrix_mul(m_a, m_b):
    """ func matrix

    Args:
        m_a: first character to be checked
        m_b: second character to be checked
    Raise:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        TypeError: If m_a or m_b is empty.
        TypeError: If m_a or m_b has different-sized rows.
        ValueError: If m_a , m_b cannot be multiplied.
    return:
        A new matrix
    """

    if m_a == [] or m_a == [[]]:

        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:

        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):

        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):

        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):

        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(r, list) for r in m_b):

        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(e, int) or isinstance(e, float))
            for e in [n for r in m_a for n in r]):

        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(e, int) or isinstance(e, float))
    for e in [n for r in m_b for n in r]):

        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):

        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(r) == len(m_b[0]) for r in m_b):

        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):

        raise ValueError("m_a and m_b can't be multiplied")

    new_b = []
    for x in range(len(m_b[0])):
        n_r = []

        for i in range(len(m_b)):

            n_r.append(m_b[i][x])
        new_b.append(n_r)

    n_mat = []

    for r in m_a:
        n_r = []

        for y in new_b:
            xx = 0

            for a in range(len(new_b[0])):
                xx += r[a] * y[a]

            n_r.append(xx)
        n_mat.append(n_r)
    return n_mat
