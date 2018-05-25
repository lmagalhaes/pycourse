# **MODULES & PACKAGES**
In python there are basically three different levels of namespaces:
* Script: The context the main script is running
* Package: The \__init__.py file
* Module: The files inside the package


## [__PEP 8 -- Style Guide for Python for packages and modules Code__](https://www.python.org/dev/peps/pep-0008/)

* Naming convention for Packages and Modules:
    * No spaces
    * All lowercase
* Public and "Private"
    * By default all names are public
    * Names starting with underscores "\_" are not meant to be used directly and thus should be avoided

### __TL;DR__

* Import whole packages: `import mypackage`
* Import whole modules: `from mypackage import mymodule`
* Import labels from inside a given module: `from mypackage.mymodule import myfunction`
*
