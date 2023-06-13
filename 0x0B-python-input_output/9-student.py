#!/usr/bin/python3
""" module of student class"""


class Student:
    """class student with attr and methods"""

    def __init__(self, first_name, last_name, age):
        """init metode that initate attr
            Attr:
                first_name: first name of student
                last_name: last name of student
                age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public intance method that get dictionary
            description of class
        """
        return vars(self)
