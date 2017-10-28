Konichiwa is "Hello World" Done Right
=====================================

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
to approximately:

1. 100 lines for the core module
2. 150 lines of unit tests
3. 50 lines of package configuration
4. 150 lines of documentation

Plus thousands more lines of auto-generated config files, boilerplate
legalese, and other project artifacts.

To be fair, about half of this is fixed cost overhead that doesn't expand with
the size of the project, while the other half, like unit tests and
documentation scale linearly and appropriately with project size. Also, for
widely used projects (large or small) all of these are a good idea.  But the
absurdity of applying all the same recommendations to small, less widely
distributed packages is evident in the 500:1 inflation ratio we see when we
apply to an extreme case.


Features
--------

- README
- open source license
- semantic versioning
- command line interface:
    - convenient -cli script installed on PATH
    - GNU inspired options (--help, --version, and --verbose)
    - Python stack trace suppressed by default
- full pep8 compliance via pylint
- module-level logging
- distutils compatability
- semi-automated documentation via Sphinx
- Travis CI integration
- full suite of unit tests (unittest and doctest)
- full code coverage
- package name is short, unique, and almost completely opaque
- tons of little hidden config files in the project root folder


Resources & Inspirations
------------------------
- https://gist.github.com/sloria/7001839
- https://www.python.org/dev/peps/pep-0257/
- https://www.python.org/dev/peps/pep-0008/
- https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html
- https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
- https://www.python.org/dev/peps/pep-0396/
- http://semver.org/
- https://packaging.python.org/guides/migrating-to-pypi-org/#uploading
- https://travis-ci.org/
- https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
