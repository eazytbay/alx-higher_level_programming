#!/usr/bin/python3
"""Max_integer([..]) unittest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class unittest for max_integer"""
    def test_module_docstring(self):
        """Module docsting Test"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """docstring function test"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Empty list [] test"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """No arguments test passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Only one number test in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """Tests for positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """All positive test with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_beginning(self):
        """All positive test with max at beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """List test with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """List test with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-integer type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
