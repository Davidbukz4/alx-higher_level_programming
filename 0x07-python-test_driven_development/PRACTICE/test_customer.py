#!/usr/bin/python3

import unittest
from customer import Customer

class TestCustomerClass(unittest.TestCase):
    
    def setUp(self):
        self.customer_1 = Customer('Tom', 'Dickson', 5000)
        self.customer_2 = Customer('Harry', 'Potter', 3000)

    def test_customer_mail(self):
        self.assertEqual(self.customer_1.customer_mail, 'Tom.Dickson@email.com')
        self.assertEqual(self.customer_2.customer_mail, 'Harry.Potter@email.com')

    def test_customer_fullname(self):
        self.assertEqual(self.customer_1.customer_fullname, 'Tom Dickson')
        self.assertEqual(self.customer_2.customer_fullname, 'Harry Potter')

    def test_apply_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()
 
        self.assertEqual(self.customer_1.purchase, 4750)
        self.assertEqual(self.customer_2.purchase, 2850)

if __name__ == "__main__":
    unittest.main()
