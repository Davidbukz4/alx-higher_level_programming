#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Performs unittest for ma_integer([..])"""
    def setUp(self):
        """sets up properties"""
        test_list = [11, -2, 43, 4, -14, 34]
        self.test_list = test_list

    def test_returnVal(self):
        """checks if function returned something"""
        self.assertIsNotNone(max_integer(self.test_list))

    def test_outputVal(self):
        """checks that output value is correct"""
        temp = self.test_list[0]
        for i in range(1, len(self.test_list)):
            if temp < self.test_list[i]:
                temp = self.test_list[i]
        self.assertEqual(max_integer(self.test_list), temp)

    def test_emptyList(self):
        """checks output for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_oneElement(self):
        """checks output for single element"""
        self.assertEqual(max_integer([4]), 4)

    def test_floats(self):
        """tests the output for float"""
        self.assertEqual(max_integer([1.2, 1.4, 1.3, 1.1]), 1.4)

    def test_negFloats(self):
        """tests the output for negative floats"""
        self.assertEqual(max_integer([-1.2, -1.4, -1.3, -1.1]), -1.1)

    def test_sameNum(self):
        """tests the output for same numbers"""
        self.assertEqual(max_integer([33, 33, 33, 33]), 33)

    def test_sameNumNeg(self):
        """tests the output for same negative numbers"""
        self.assertEqual(max_integer([-33, -33, -33, -33]), -33)

    def test_strList(self):
        """tests string inside list"""
        self.assertEqual(max_integer(["dave"]), "dave")

    def test_string(self):
        """tests the output for string"""
        self.assertEqual(max_integer("dave"), "v")

    def test_tuple(self):
        """tests the output for tuple"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_multiTuples(self):
        """tests the output for multiple tuples"""
        self.assertEqual(max_integer([(3, 4, 5), (8, 3, 2)]), (8, 3, 2))

    def test_noneInput(self):
        """test none as input"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_num(self):
        """test a number as input"""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()
