# 0x0A-python-inheritance

### Requirements

#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

#### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

#### Documentation
- Do not use the words import or from inside your comments, the checker will think you try to import some modules

---

### Task:

#### 0-lookup.py
Write a function that returns the list of available attributes and methods of an object:

- Prototype: def lookup(obj):
- Returns a list object
- You are not allowed to import any module
- No test cases needed

#### 1-my_list.py, tests/1-my_list.txt
Write a class MyList that inherits from list:

- Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type int
- You are not allowed to import any module

#### 2-is_same_class.py
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

- Prototype: def is_same_class(obj, a_class):
- You are not allowed to import any module
- No test cases needed

#### 3-is_kind_of_class.py
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

- Prototype: def is_kind_of_class(obj, a_class):
- You are not allowed to import any module
- No test cases needed

#### 4-inherits_from.py
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

- Prototype: def inherits_from(obj, a_class):
- You are not allowed to import any module
- No test cases needed

#### 5-base_geometry.py
Write an empty class BaseGeometry.

- You are not allowed to import any module
- No test cases needed

#### 6-base_geometry.py
Write a class BaseGeometry (based on 5-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- You are not allowed to import any module
- No test cases needed

#### 7-base_geometry.py, tests/7-base_geometry.txt
Write a class BaseGeometry (based on 6-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- Public instance method: def integer_validator(self, name, value): that validates value:
-- you can assume name is always a string
-- if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
-- if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
- You are not allowed to import any module

#### 8-rectangle.py
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

- Instantiation with width and height: def __init__(self, width, height):
-- width and height must be private. No getter or setter
-- width and height must be positive integers, validated by integer_validator
- No test cases needed

#### 9-rectangle.py
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

- Instantiation with width and height: def __init__(self, width, height)::
-- width and height must be private. No getter or setter
-- width and height must be positive integers validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
- No test cases needed

#### 10-square.py
Write a class Square that inherits from Rectangle (9-rectangle.py):

- Instantiation with size: def __init__(self, size)::
-- size must be private. No getter or setter
-- size must be a positive integer, validated by integer_validator
- the area() method must be implemented
- No test cases needed

#### 11-square.py
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

- Instantiation with size: def __init__(self, size)::
-- size must be private. No getter or setter
-- size must be a positive integer, validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the square description: [Square] <width>/<height>
