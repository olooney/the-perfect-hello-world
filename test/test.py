import unittest
import sys
from io import StringIO
from .capture import captured_output
from the_perfect_hello_world.hello_world import HelloWorld, parse_hello_world_args
 
class TestHelloWorld(unittest.TestCase):

    def test_defaults(self):
        hello = HelloWorld()
        self.assertEqual(hello.greet(), 'Hello World!')

    def test_state(self):
        # constructor
        hello = HelloWorld('XYZ', '?')

        # persistence
        self.assertEqual(hello.greet('ABC'), 'XYZ ABC?')
        self.assertEqual(hello.greet(target='DEF'), 'XYZ DEF?')

    def test_constructor_kwargs(self):
        # constructor
        hello = HelloWorld(greeting='XYZ', punctuation='?')
        # attributes
        self.assertEqual(hello.greeting, 'XYZ')
        self.assertEqual(hello.punctuation, '?')
        self.assertEqual(hello.greet(), 'XYZ World?')

    def test_public_attributes(self):
        hello = HelloWorld('XYZ', '?')

        # read attributes
        self.assertEqual(hello.greeting, 'XYZ')
        self.assertEqual(hello.punctuation, '?')

        # write attributes
        hello.greeting = 'IJK'
        self.assertEqual(hello.greet('DEF'), 'IJK DEF?')
        hello.punctuation = ':'
        self.assertEqual(hello.greet('DEF'), 'IJK DEF:')


    def test_print_default(self):
        hello = HelloWorld()

        with captured_output() as (out, err):
            hello.print_greeting()
            hello.print_greeting('Python')
        self.assertEqual(out.getvalue(), 'Hello World!\nHello Python!\n')
        self.assertEqual(err.getvalue(), '')

    def test_print_default(self):
        hello = HelloWorld()
        psuedofile = StringIO()

        with captured_output() as (out, err):
            hello.print_greeting('STDOUT')
            hello.print_greeting('STDERR', file=sys.stderr)
            hello.print_greeting('FILE', file=psuedofile)
        self.assertEqual(out.getvalue(), 'Hello STDOUT!\n')
        self.assertEqual(err.getvalue(), 'Hello STDERR!\n')
        self.assertEqual(psuedofile.getvalue(), 'Hello FILE!\n')


class TestParseArg(unittest.TestCase):

    def test_defaults(self):
        args = parse_hello_world_args([])
        self.assertIs(args.verbose, False)
        self.assertEqual(args.greeting, 'Hello')
        self.assertEqual(args.target, 'World')
        self.assertEqual(args.punctuation, '!')

    def test_verbose(self):
        args = parse_hello_world_args(['-v'])
        self.assertIs(args.verbose, True)

    def test_all(self):
        args = parse_hello_world_args('-v -p ? -g Bonjour Monde'.split())
        self.assertIs(args.verbose, True)
        self.assertEqual(args.greeting, 'Bonjour')
        self.assertEqual(args.target, 'Monde')
        self.assertEqual(args.punctuation, '?')

    def test_version(self):
        with captured_output() as (out, err):
            with self.assertRaises(SystemExit):
                args = parse_hello_world_args(['--version'])
        self.assertRegex(out.getvalue(), '\d+\.\d+\.\d+')

    def test_positional_error(self):
        with captured_output() as (out, err):
            with self.assertRaises(SystemExit) as raised:
                args = parse_hello_world_args('too many positional arguments'.split())
            self.assertGreater(raised.exception.code, 0)
        self.assertRegex(err.getvalue(), 'unrecognized arguments')

    def test_option_error(self):
        with captured_output() as (out, err):
            with self.assertRaises(SystemExit) as raised:
                args = parse_hello_world_args('-q --broken'.split())
            self.assertGreater(raised.exception.code, 0)
        self.assertRegex(err.getvalue(), 'unrecognized arguments')
        

 
if __name__ == '__main__':
    unittest.main()
