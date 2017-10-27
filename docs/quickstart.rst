.. _quickstart:

Quick Start
===========

Command line:

.. code-block:: bash
    
    pip install the_perfect_hello_world

Import:

.. code-block:: python
    
    from the_perfect_hello_world.hello_world import HelloWorld


Basic usage:

.. doctest::
>>> hello = HelloWorld()
>>> hello.greet()
'Hello World!'

We can also use various options to format our greeting:

.. doctest::
>>> bonjour = HelloWorld(greeting='Bonjour', punctuation='.')
>>> bonjour.greet("le Monde")
'Bonjour le Monde.'

