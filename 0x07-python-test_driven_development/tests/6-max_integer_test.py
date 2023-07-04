#!/usr/bin/python3
""" unittest for max_integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ define unittest for max """

    def test_ordered(self):
        """ test ordered """
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unordered(self):
        """ test unordered """
        unord = [1, 2, 4, 3]
        self.assertEqual(max_integer(unord), 4)

    def test_max(self):
        """ test """
        beg = [4, 3, 2, 1]
        self.assertEqual(max_integer(beg), 4)

    def test_empty(self):
        """ test """
        em = []
        self.assertEqual(max_integer(em), None)

    def test_one(self):
        """ test """
        one = [7]
        self.assertEqual(max_integer(one), 7)

    def test_float(self):
        """ test """
        fl = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(fl), 15.2)

    def test_int_float(self):
        """ tests """
        num = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(num), 15.5)

    def test_string(self):
        """ test """
        stri = "Brennan"
        self.assertEqual(max_integer(stri), 'r')

    def test_strings(self):
        """ tests """
        stri = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(stri), "name")

    def test_empty_st(self):
        """ tests """
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
