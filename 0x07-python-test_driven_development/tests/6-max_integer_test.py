#!/usr/bin/python3
""" Unittests for max_integer([..]). """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ define unittests for max_integer([..]) """

    def test_order(self):
        """ test ordered list """
        ord = [1, 2, 3, 4]
        self.assertEqual(max_integer(ord), 4)

    def test_unorder(self):
        """ test unorder lists """
        unord = [1, 2, 4, 3]
        self.assertEqual(max_integer(unord), 4)

    def test_max(self):
        """ tests the max at the beginning """
        mx = [4, 3, 2, 1]
        self.assertEqual(max_integer(mx), 4)

    def test_empty(self):
        """ test an empty list """
        em = []
        self.assertEqual(max_integer(em), None)

    def test_onlyelem(self):
        """ test a list with one element """
        only = [7]
        self.assertEqual(max_integer(only), 7)

    def test_float(self):
        flo = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(flo), 15.2)

    def test_int_flo(self):
        """ test a list of int and floats """
        num = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(num), 15.5)

    def test_stri(self):
        """ test of a string """
        stri = "Brennan"
        self.assertEqual(max_integer(stri), 'r')

    def test_strings(self):
        """ test of list of string """
        strin = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strin), "name")

    def test_empty_list(self):
        """ test an empty string """
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
