#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_end(self):
        """Test when the max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_mixed_int_float(self):
        """Test a list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)
