## lists

List is an ordered collection of items and can contain any sequence of any valid python types,including.

Elements in a list should be enclosed by square brackets separated by ',', including others lists.

e.g 
```python
my_list = ["one", 2, 3.0, False, []]
```

Python list are considered a mutable type because, which mean we it can be altered once you create a list you can add, remove and search for elements.

As everything else in Python, a list is an object. That means a list has attributes and methods.

Some important methods to manipulate a list are:

* append - Adds an element to the end of the list

* insert - Adds an element to a certain position of the lists

* copy - Returns a copy of a list

* pop - Removes and returns the last element of a list

* clear - Removes all elements in a list


You can have a fuill of methods and attributes using the dir function:
```python
dir([])
```

```python
my_list = [1, 2] # Creates a list with the numbers 1, 2

my_list.insert(0, 0) # Insert number 0 to the first position of the list

my_list.append(3) # Add number 3 on the last position of the list

print my_list # [0, 1, 2, 3]

my_list.remove(2) # Removes the first occurence of the number 2 from the list
```

To count elements in a list 
