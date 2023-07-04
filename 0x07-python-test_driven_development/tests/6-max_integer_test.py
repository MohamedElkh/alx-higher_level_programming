#!/usr/bin/python3
""" import unittest for max integer """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ define unittest for max_integer """

    def ordered_list(self):
        """ test ordered list """
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def unordered_list(self):
        """ define unordered test """
        unorder = [1, 2, 4, 3]
        self.assertEqual(max_integer(unorder), 4)

    def max_in_thebegin(self):
        """ define the max value """
        maxx = [4, 3, 2, 1]
        self.assertEqual(max_integer(maxx), 4)

    def empty_list(self):
        """ test empty list """
        m = []
        self.assertEqual(max_integer(m), None)

    def one_elem_inlist(self):
        """ test the list with a single element """
        elem = [7]
        self.assertEqual(max_integer(elem), 7)

    def tests_float(self):
        """ test the list of floats """
        flo = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(flo), 15.2)

    def func_int_floats(self):
        """ tests a list int and floats """
        in_flo = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(in_flo), 15.5)

    def func_string(self):
        """ tests the string """
        stri = "Brennan"
        self.assertEqual(max_integer(stri), 'r')

    def list_of_string(self):
        """ test a list of string """
        stri = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(stri), "name")

    def empty_string_test(self):
        """ tests an empty string """
        self.assertEqual(max_integer(""), None)

if __name__ =='__main__':
    unittest.main()
