#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer function
    """

    def test_empty_list(self):
        """
        Test if the function handles an empty list correctly
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_integers(self):
        """
        Test if the function returns the highest positive integer from a list
        """
        result = max_integer([1, 4, 5, 3])
        self.assertEqual(result, 5)

    def test_negative_integers(self):
        """
        Test if the function returns the highest negative integer from a list
        """
        result = max_integer([-2, -4, -1, -5])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        """
        Test if the function returns the highest integer (positive or negative) from a list
        """
        result = max_integer([-2, 4, -1, 5])
        self.assertEqual(result, 5)

    def test_duplicate_integers(self):
        """
        Test if the function returns the highest integer from a list with duplicate values
        """
        result = max_integer([2, 4, 2, 4])
        self.assertEqual(result, 4)

    def test_floats(self):
        """
        Test if the function returns the highest float from a list
        """
        result = max_integer([2.75, 4.25, 1.25, 5.5])
        self.assertEqual(result, 5.5)

    def test_strings(self):
        """
        Test if the function returns the highest string from a list
        """
        result = max_integer(['a', 'A', 'r', 'R'])
        self.assertEqual(result, 'r')

    def test_mixed_types(self):
        """
        Test if the function returns the highest value (integer, float, or string) from a list with mixed types
        """
        result = max_integer([2, 4.25, 'r', -5])
        self.assertEqual(result, 'r')


if __name__ == "__main__":
    unittest.main()
