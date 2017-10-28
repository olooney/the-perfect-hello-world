.. _quickstart:

Quick Start
===========

Command line:

.. code-block:: bash
    
    pip install konichiwa 

Import:

.. code-block:: python

   from konichiwa import HelloWorld


Basic usage:

>>> hello = HelloWorld()
>>> hello.greet()
'Hello World!'

We can also use various options to format our greeting:

>>> bonjour = HelloWorld(greeting='Bonjour', punctuation='.')
>>> bonjour.greet("le Monde")
'Bonjour le Monde.'

