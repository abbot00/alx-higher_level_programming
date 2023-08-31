#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test when the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_same_elements(self):
        """Test with a list containing repeated elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_floats(self):
        """Test with a list containing floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 4.2]), 4.2)
        self.assertEqual(max_integer([-1.5, -2.7, -0.3, -4.2]), -0.3)

    def test_mixed_integers_and_floats(self):
        """Test with a list containing mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)
        self.assertEqual(max_integer([-1, -2.5, -3, -4.7]), -1)
        self.assertEqual(max_integer([0, 0.5, 0, -0.5]), 0.5)

    def test_mixed_types(self):
        """Test with a list containing mixed data types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4])


if __name__ == '__main__':
    unittest.main()
