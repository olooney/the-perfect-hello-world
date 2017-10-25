Hello World, Ruined by "Best Practices"
---------------------------------------

Python's one line ``print("Hello World!")`` has long been famous, but I wanted to
see how much overhead (boilerplate) would be generated if I followed ALL of the
recommended best practices for documenting, packaging, testing, logging, error
handling, and otherwise annotating a Python project.

Caveat: I know as well as you do that no one would recommend doing all this
stuff for such a simple project. But I think it illustates a point about how
mature (and therefore complex) the entire Python toolchain has become.

Incidently (and this was not at all the goal when I wrote it, just a nice
side effect) it illustates a typical Python project layout fairly well,
so if you're at the stage of learning Python where you start to wonder
about how to best organize your projects... well, you could do worse than
this project, but there are many good tutorials available.


TODO
----
- [X] LICENSE
- [X] README.md
- [X] .gitignore
- [X] bin script
- [X] setup.py
- [ ] unit tests
- [X] pylint
- [X] pep8
- [X] --help and --version 

- [X] requirements.txt
- [ ] docs
- [X] module-level logging
- [X] real docstrings
- [ ] code coverage
- [ ] travis.yml
- [ ] setup.cfg?

