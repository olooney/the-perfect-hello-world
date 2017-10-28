import unittest
import doctest
import konichiwa

finder = doctest.DocTestFinder(recurse=True)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(konichiwa))
    return tests

if __name__ == '__main__':
    doctest.testmod()
