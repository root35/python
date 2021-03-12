import unittest


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

    def formal_name(self, title):
        return title + " " + self.full_name()


class TestPerson(unittest.TestCase):
    def test_main(self):
        guy = Person("John", "Doe")
        self.assertEqual("John", guy.first)
        self.assertEqual("Doe", guy.last)
        self.assertEqual("John Doe", guy.full_name())
        self.assertEqual("Mr. John Doe", guy.formal_name("Mr."))


# -- USAGE: python -m unittest test-with-unittest.py
