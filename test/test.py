import unittest
from the_perfect_hello_world.hello_world import HelloWorld
 
class TestBasicFunction(unittest.TestCase):
    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        hello = HelloWorld()
        self.assertEqual(hello.greet(), 'Hello World!')

    def test_3(self):
        bonjour = HelloWorld(greeting='Bonjour')
        self.assertEqual(bonjour.greet(), 'Bonjour World!')
 
if __name__ == '__main__':
    unittest.main()
