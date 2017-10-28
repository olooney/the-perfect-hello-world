.. _quickstart:

Quick Start
===========

Install:

.. code-block:: bash
    
    pip install --extra-index-url https://testpypi.python.org/pypi konichiwa 

Command Line Interface:

.. code-block:: bash
    
    $ konichiwa-cli
    Hello World
    $ konichiwa-cli --help

Import:

.. code-block:: python

API Usage:

>>> from konichiwa import HelloWorld
>>> hello = HelloWorld()
>>> hello.greet()
'Hello World!'

We can also use various options to format our greeting:

>>> bonjour = HelloWorld(greeting='Bonjour', punctuation='.')
>>> bonjour.greet("le Monde")
'Bonjour le Monde.'

