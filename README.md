# pycourse

## Dependencies

* docker
* docker-compose

## Running ipython shell

docker-compose run --rm pycourse

### Topics

1. [Introduction](./1-introduction)

2. [Installation](./2-installation)

3. Python Basics
    * What are strong typed languages?
    * EVERYTHING IS A FREAKING OBJECT
    * EVEN OBJECT IS AN OBJECT
    * "1" + 1 = `must be str, not int`
    * PHP dynamically typed vs Python strong types
    * Strong typed languages vs Statically typed languages
    * Data structures
    * Dict
    * List
    * Set
    * Collections
    * Introduction t0 "comprehensions"

4. Classes and functions
    * \__init__
    * "Be public"
        * EVERYTHING IS PUBLIC
        * But that's a good thing
    * Private" classes
        * "You don't need too many classes"
    * Functions as first citizen
        * Functions are objects!
    * Named parameters name=value
    * Dict and List expansion **
    * Magic methods
    * Reference vs "Labels"
        * Names and bindings
        * Variables and assisgnment
    * Override methods

5. Super aka. super()
    * It's more than you think
    * Multiple inheritance
    * NOT "TRAITS"
    * If you need it, there's 80% change you are doing it wrong
    * MRO - Method resolution order

6. PYTHONPATH, IMPORT PATH:
    * How does it work?
    * Entrypoint concept
    * Setup.py "entry_point"
    * Python file outside package

7. Packages:
    * import package
    * __init__.py
    * Add variables when importing the module

8. Modules:
    * from package import module
    * import

9. Typing

10. TESTING:
    * Unittest module
    * Runners:
        * Pytest
        * Tox

11. Interesting tools:
    * Micro: Flask
    * Big: Django
    * Async: AIOHTTP, Tornado, Twisted

12. Dependency Management and Distribution
    * Pip
    * Pipenv
    * setuptools

13. DI
    * Not as needed as you would think
    * Parameters vs Imports
    * Modules are factories

14. Extras:
    *Design Patterns
        * How not to write Python
    * Multi-threaded/processed applications: How not to
        * Threads
        * Processes
        * Async
        * GIL
    * OOP flavour
        * Access over responsibility
