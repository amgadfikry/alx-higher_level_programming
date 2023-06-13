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

    def to_json(self, attrs=None):
        """ public intance method that get dictionary
            description of class
        """
        dic = vars(self)
        new_dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return dic
            for key, value in dic.items():
                if key in attrs:
                    new_dic[key] = value
            return new_dic
        return dic

    def reload_from_json(self, json):
        """ public instance that replace attributes by
            attributes in json
        """
        for key, value in json.items():
            self.key = value
