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
    name='the_perfect_hello_world',
    version='1.0.0',
    author='Oran Looney',
    author_email='olooney@gmail.com',
    packages=['the_perfect_hello_world'],
    test_suite='tests',
    cmdclass={
        'pylint': PyLintCommand,
    }
)
