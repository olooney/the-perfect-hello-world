Konichiwa is "Hello World" Done Right(tm)
=========================================

Python has long been famous for having a one line "Hello World!", contrasting
it to the boilerplate of Java or C++.

.. code-block:: python

  print("Hello World!")

But that's woefully inadequate these days. To turn this humble
script into a Real Project, we need to apply a generous slathering
of Best Practices. And by "best practice," I mean any reasonable
guideline ever expounded by anyone at any time, regardless of context
or relevance to this project, or even plausible applicability to a 
project of such limited scope.

The best way to make the case in favor of the intelligent and limited
use of bells of whistles is to show just how overwhelming it can
be when all possible boilerplate is included without thought. This
projects "natural" length is one line of code and yet, simply by
rigidly adhering to countless guidelines, we managed to expand that
to:

1. 100 lines for the core module
2. 150 lines of unit tests
3. 50 lines of package configuration
4. 150 lines of documentation

Plus thousands more lines of auto-generated config files, boilerplate
legalese, and other project artifacts.


Features
--------

- README
- open source license
- command line interface:
    - convenient -cli script installed on PATH
    - GNU inspired options (--help, --version, and --verbose)
- full pylint and pep8 compliance
- module-level logging
- distutils compatability
- semi-automated documentation via Sphinx
- Travis CI integration
- full suite of unit tests (unittest and doctest)
- full code coverage
- lots of little hidden config files in the project root folder



Konichiwa is feature complete!

- [X] LICENSE
- [X] README.md
- [X] .gitignore
- [X] bin script
- [X] setup.py
- [X] unit tests
- [X] pylint
- [X] pep8
- [X] --help and --version 
- [X] requirements.txt
- [X] docs
- [X] module-level logging
- [X] real docstrings
- [X] code coverage
- [X] travis.yml

https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
