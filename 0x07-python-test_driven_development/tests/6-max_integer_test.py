#!/usr/bin/python3
""" test module for function find biggest integer in list"""
import unittest
mi = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class object inherit from unittest testcase"""

    def test_empty(self):
        """methode test empty cases and no args"""
        self.assertIsNone(mi())
        self.assertIsNone(mi([]))

    def test_normal_cases(self):
        """ method that test normal cases"""
        self.assertEqual(mi([1, 3, 5, 10]), 10)
        self.assertEqual(mi([1, -3, -5, -10]), 1)
        self.assertEqual(mi([1.8, 3.8, -5.8, -10.9]), 3.8)
        self.assertEqual(mi([-1, -3, -5, -10, 0]), 0)
