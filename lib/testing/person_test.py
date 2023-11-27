# person_test.py

import unittest
from person import Person  # Assuming your Person class is in a file named person.py

class TestPerson(unittest.TestCase):
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person(name="Guido")  # Provide a name argument
        self.assertEqual(type(guido), Person)

if __name__ == '__main__':
    unittest.main()
