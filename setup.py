#!/usr/bin/env python

from setuptools import setup
from distutils.cmd import Command
import subprocess
import konichiwa

class PyLintCommand(Command):
    """Adaptor to expose pylint as a setup.py command"""

    description = "run pylint on this project"
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass
    
    def run(self):
        subprocess.run(["pylint", "konichiwa"])

setup(
    # meta
    name='konichiwa',
    version=konichiwa.__version__,
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
    packages=['konichiwa'],
    scripts=['bin/konichiwa-cli'],
    entry_points = {
        'console_scripts': [
            'konichiwa-cli = konichiwa:main'
        ]
    },
    test_suite='test',
    cmdclass={
        'pylint': PyLintCommand,
    }
)
