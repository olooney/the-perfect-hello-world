'''
module doc string goes here
'''

import logging
import argparse
import sys


class HelloWorld:
    '''
    class docstring goes here
    '''

    def __init__(self, greeting='Hello', punctuation='!'):
        'constructor docstring goes here'

        self.greeting = greeting
        self.punctuation = punctuation 


    def greet(self, target='World'):
        'method docstring goes here'

        return '{self.greeting} {target}{self.punctuation}'.format(**locals())


    def print_greeting(self, target='World', output_file=sys.stdout):
        'method docstring goes here'
        
        print(self.greet(target), file=output_file)

        
def parse_hello_world_args(argv=sys.argv[1:]):
    '''
    parse function docstring goes here
    '''

    parser = argparse.ArgumentParser(description='Hello World CLI', add_help=True)

    # a single optional position argument
    parser.add_argument('target', metavar='TARGET', nargs='?', default='World')

    # 'version' is special, like --help. argparse will print the version message and exit 0.
    parser.add_argument('--version', action='version', version="%(prog)s 1.0.0")

    # other options
    parser.add_argument('-g', '--greeting', type=str, dest='greeting', default='Hello', help="change the greeting verb")
    parser.add_argument('-p', '--punctuation', type=str, dest='punctuation', default='!', choices=['!', '.', '?'])
    parser.add_argument('-o', '--output', dest='output_file', metavar='FILE', type=argparse.FileType('w'), default=sys.stdout, help="save greeting to the given file")
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', default=False, help="prints additional diagnostic messages to stderr")
    return parser.parse_args(argv)
        

if __name__ == '__main__':
    try:
        args = parse_hello_world_args()
    except Exception as ex:
        print(ex)
        sys.exit(1)

    # TODO configure logging at an appropriate level now that we know verbose

    try:
        hw = HelloWorld(args.greeting, args.punctuation)
        hw.print_greeting(args.target, output_file=args.output_file)
        if args.output_file != sys.stdout:
            args.output_file.close()
    except Exception as ex:
        print(ex)
        sys.exit(1)


__all__ = ['HelloWorld', 'parse_hello_world_args']



