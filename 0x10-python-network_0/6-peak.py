#!/usr/bin/python3
""" find the peak in a list of unsorted ints """


def find_peak(list_of_integers):
    """
    args:
        list_of_integers: list of integers to find peak
    Return: peak of list_of_intehers or none
    """
    sz = len(list_of_integers)
    m_el = sz
    mile = sz // 2

    if sz == 0:
        return None

    while True:
        m_el = m_el // 2
        if (mile < sz - 1 and
                list_of_integers[mile] < list_of_integers[mile + 1]):
            if m_el // 2 == 0:
                m_el = 2
            mile = mile + m_el // 2
        elif m_el > 0 and list_of_integers[mile] < list_of_integers[mile - 1]:
            if m_el // 2 == 0:
                m_el = 2
            mile = mile - m_el // 2
        else:
            return list_of_integers[mile]
