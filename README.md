# pycourse

## Dependencies

* docker
* docker-compose

## Running ipython shell

docker-compose run --rm pycourse

### What is python
* Brief python backstory
* The Zen of Python (PEP 20)
    * Beautiful is better than ugly
    * Explicit is better than implicit
    * Simple is better than complex
    * Complex is better than complicated
    * Readability counts

### Overall python:
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
* Introduction to "comprehensions"

### CLASSES/FUNCTIONS:
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
    * PHP Reference "&" vs Python's
* Override methods

### Super aka. super()
* It's more than you think
* Multiple inheritance
* NOT "TRAITS"
* If you need it, there's 80% change you are doing it wrong
* MRO - Method resolution order

### PYTHONPATH, IMPORT PATH:
* How does it work?
* Entrypoint concept
* Setup.py "entry_point"
* Python file outside package

### Packages:
* import package
* __init__.py
* Add variables when importing the module

### Modules:
* from package import module
* import

### TESTING:
* Runners:
    * Pytest
    * Tox

### Interesting tools:
Micro: Flask
Big(o): Django
IoHTTP, Tornado, Twisted

### Dependency Management
Pip
Pipenv

### DI
* Not as needed as you would think
* Parameters vs Imports
* Modules as factories

### Extras:
* How not to write Python as PHP
* Design Patterns
* Multi-processed applications: How not to
    * Threads
    * Processes
    * GIL
* OOP flavour
* PHP
* Restriction over responsibility
* Python
* Access over responsibility
