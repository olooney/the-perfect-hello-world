#!/usr/bin/env python

from setuptools import setup
from distutils.cmd import Command
import subprocess

class PyLintCommand(Command):
    """Adaptor to expose pylint as a setup.py command"""

    description = "run pylint on this project"
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass
    
    def run(self):
        subprocess.run(["pylint", "the_perfect_hello_world"])

setup(
    # meta
    name='the_perfect_hello_world',
    version='1.0.0',
    author='Oran Looney',
    author_email='olooney@gmail.com',
    url='https://github.com/olooney/the-perfect-hello-world',
    description='"Hello World" ruined by too many "best practices."',
    long_description=open('README.rst').read(),
    license="Apache License 2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
    ],

    # technical
    packages=['the_perfect_hello_world'],
    scripts=['bin/hello-world-cli'],
    test_suite='test',
    cmdclass={
        'pylint': PyLintCommand,
    }
)
