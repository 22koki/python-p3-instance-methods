#!/usr/bin/env python3

import io
import sys
import types
import unittest
from dog import Dog

class TestDog(unittest.TestCase):
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog(name="Fido")  # Provide a name argument
        self.assertEqual(type(fido), Dog)

class TestBark(unittest.TestCase):
    '''Dog.bark() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog(name="Fido")  # Provide a name argument
        self.assertTrue(isinstance(fido.bark, types.MethodType))

    def test_prints_woof(self):
        '''prints "Woof!"'''
        fido = Dog(name="Fido")  # Provide a name argument
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()  # Call bark as a method
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Woof!\n")

class TestSit(unittest.TestCase):
    '''Dog.sit() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog(name="Fido")  # Provide a name argument
        self.assertTrue(isinstance(fido.sit, types.MethodType))

    def test_prints_the_dog_is_sitting(self):
        '''prints "The dog is sitting."'''
        fido = Dog(name="Fido")  # Provide a name argument
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.sit()  # Call sit as a method
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The dog is sitting.\n")

if __name__ == '__main__':
    unittest.main()
