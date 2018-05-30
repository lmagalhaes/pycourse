# pycourse

## Dependencies

* docker
* docker-compose

## Running ipython shell

docker-compose run --rm pycourse

### Topics

1. [What is python](./1-what-is-python)

2. Python Basics
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

3. Classes and functions
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

4. Super aka. super()
    * It's more than you think
    * Multiple inheritance
    * NOT "TRAITS"
    * If you need it, there's 80% change you are doing it wrong
    * MRO - Method resolution order

5. PYTHONPATH, IMPORT PATH:
    * How does it work?
    * Entrypoint concept
    * Setup.py "entry_point"
    * Python file outside package

6. Packages:
    * import package
    * __init__.py
    * Add variables when importing the module

7. Modules:
    * from package import module
    * import

8. TESTING:
    * Unittest module
    * Runners:
        * Pytest
        * Tox

9. Interesting tools:
    * Micro: Flask
    * Big: Django
    * Async: AIOHTTP, Tornado, Twisted

10. Dependency Management and Distribution
    * Pip
    * Pipenv
    * setuptools

11. DI
    * Not as needed as you would think
    * Parameters vs Imports
    * Modules are factories

11. Extras:
    11.1 Design Patterns
        * How not to write Python
    11.2 Multi-threaded/processed applications: How not to
        * Threads
        * Processes
        * Async
        * GIL
    11.3 OOP flavour
        * Access over responsibility
