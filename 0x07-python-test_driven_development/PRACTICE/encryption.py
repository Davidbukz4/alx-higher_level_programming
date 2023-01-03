#!/usr/bin/python3

import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "I am Batman!!! 888"
    # test if inout exists
    def test_inputType(self):
        self.assertIsNotNone(self.my_message)
    # checks input types
    def test_checkType(self):
        self.assertIsInstance(self.my_message, str)
    # test if function returned something
    def test_returnYes(self):
        self.assertIsNotNone(encrypt(self.my_message))
    # checks length of message input and output is equal
    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))
    # checks if input and output are different
    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))
    # checks output types must be string
    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)
    # checks if message was encrypted
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message, encrypt(self.my_message))


if __name__ == "__main__":
    unittest.main()
