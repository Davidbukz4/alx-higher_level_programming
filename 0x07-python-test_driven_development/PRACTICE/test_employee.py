#!/usr/bin/python3

import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployeeClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """It runs only once in the program i.e at the beginning if the test"""
        print("setupClass")

    def setUp(self):
        """It runs before each test"""
        print("setup")
        self.emp_1 = Employee('David', 'Egwuatu', 50000)
        self.emp_2 = Employee('Dwayne', 'Johnson', 60000)

    @classmethod
    def tearDownClass(cls):
        """It runs once after all test have completed"""
        print("teardownClass\n")

    def tearDown(self):
        """It runs after each test have completed"""
        print("Teardown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, 'David.Egwuatu@email.com')
        self.assertEqual(self.emp_2.email, 'Dwayne.Johnson@email.com')

        self.emp_1.first = 'Wave'
        self.emp_2.first = 'Dada'

        self.assertEqual(self.emp_1.email, 'Wave.Egwuatu@email.com')
        self.assertEqual(self.emp_2.email, 'Dada.Johnson@email.com')
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'David Egwuatu')
        self.assertEqual(self.emp_2.fullname, 'Dwayne Johnson')

        self.emp_1.first = 'Wave'
        self.emp_2.first = 'Dada'

        self.assertEqual(self.emp_1.fullname, 'Wave Egwuatu')
        self.assertEqual(self.emp_2.fullname, 'Dada Johnson')
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        # to mark the object where they are actually used, do this instead of importing requests
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Egwuatu/May')
            self.assertEqual(schedule, 'Success')


            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Johnson/June')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == "__main__":
    unittest.main()
