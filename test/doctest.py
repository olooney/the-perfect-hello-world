import unittest
import doctest
from the_perfect_hello_world import hello_world

finder = doctest.DocTestFinder(recurse=True)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(hello_world))
    return tests
