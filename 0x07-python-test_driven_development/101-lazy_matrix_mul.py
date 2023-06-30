#!/usr/bin/python3
""" define func lazy_matrix """
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """ func lazy_matrix

    Args:
        m_a: first character
        m_b: the second character
    """

    return (n.matmul(m_a, m_b))
