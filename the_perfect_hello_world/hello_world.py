"""module doc string goes here"""

__all__ = ['HelloWorld', 'parse_hello_world_args']

import logging
import argparse
import sys

# module-level logging instance
logger = logging.getLogger(__name__) # pylint: disable=invalid-name
logger.setLevel(logging.INFO)

class HelloWorld:
    """class docstring goes here"""

    def __init__(self, greeting='Hello', punctuation='!'):
        """A flexible greeter with configurable salutation and punctuation."""

        self.greeting = greeting
        self.punctuation = punctuation
        logger.debug("New HelloWorld() object instantiated")


    def greet(self, target='World'):
        """returns a formatted greeting message as a string"""
        return '{greeting} {target}{punctuation}'.format(
            greeting=self.greeting,
            target=target,
            punctuation=self.punctuation)


    def print_greeting(self, target='World', file=sys.stdout):
        """prints the formatted greeting to a file, or stdout by default."""
        print(self.greet(target), file=file)


def parse_hello_world_args(argv):
    """returns Namespace of parsed command line arguments for the Hello World CLI"""
    parser = argparse.ArgumentParser(description='Hello World CLI', add_help=True)

    # a single optional position argument
    parser.add_argument('target', metavar='TARGET', nargs='?', default='World')

    # 'version' is special, like --help. argparse will print the version message and exit 0.
    parser.add_argument('--version', action='version', version="%(prog)s 1.0.0")

    # options
    parser.add_argument('-g', '--greeting',
                        type=str, dest='greeting', default='Hello',
                        help="change the greeting verb")
    parser.add_argument('-p', '--punctuation',
                        dest='punctuation', default='!', choices=['!', '.', '?'],
                        help="change the final character used at the end of the greeting")
    parser.add_argument('-o', '--output',
                        metavar='FILE', type=argparse.FileType('w'), default=sys.stdout,
                        help="save greeting to the given file")
    parser.add_argument('-v', '--verbose',
                        action='store_true', dest='verbose', default=False,
                        help="prints additional diagnostic messages to stderr")

    logger.debug('CLI arguments parsed successfully')

    return parser.parse_args(argv)

def main():
    """CLI handler when the module is called as a script"""
    # pylint: disable=broad-except
    try:
        args = parse_hello_world_args(sys.argv[1:])

        # upgrade logging if the verbose option is specified
        if args.verbose:
            logger.setLevel(logging.DEBUG)
            logger.addHandler(logging.StreamHandler(sys.stderr))

        logger.debug("hello_world succesfully initialized")

        # core "Hello World" functionality
        hello = HelloWorld(args.greeting, args.punctuation)
        hello.print_greeting(args.target, file=args.output)

        # argparse opened the file for us automatically but we shouldn't let it
        # dangle any longer then necesssary
        if args.output != sys.stdout:
            args.output.close()

    except Exception:
        logger.exception("hello_world has encountered an unexpected error and will exit.")
        sys.exit(1)

if __name__ == '__main__':
    main()
