#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for function max_integer"""
    def test_mod_docstring(self):
        """Check for module docstring"""
        m = __import__("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)

    def test_func_docstring(self):
        """Check for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_noargs(self):
        """no arguments passed to the function"""
        self.assertIsNone(max_integer())
