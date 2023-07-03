#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_unordered(self):
        """test unordered of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_ordered(self):
        """test ordered of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_one_element(self):
        """test list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_empty(self):
        """test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_beggining(self):
        """test a list with a begining max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_strings(self):
        """test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_strings(self):
        """test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_strings(self):
        """test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_float(self):
        """test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_int_and_float(self):
        """test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)


if __name__ == '__main__':
    unittest.main()
