#!/usr/bin/python3
""" module for base class that inhereted by classes """
import json
import csv


class Base:
    """ base class that provide super class for all
        classes
        Attr:
            nb_objects: number of instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function that start instance attrinutes
            Parameters:
                id: id of instance is none if not provided
            Atrr:
                id: attribute of id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that convert list of dictionaries
            to json string representation
            Parameters:
                list_dictionaries: list of dictionaries convert it
            Returns:
                string of list
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ static method that convert string to list of
            dictionaries
            Parameters:
                json_string: string of list of dictionaries
            Returns:
                list of dictionaries
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method that that write json string
            of list of class dictionary to file
            Parameters:
                list_objs: list of objects
        """
        dic_list = []
        if list_objs is not None:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
        with open(cls.__name__+".json", "w", encoding="utf-8") as fi:
            fi.write(cls.to_json_string(dic_list))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ class method that write csv of list of
            dictionary
            Parameters:
                list_objs: list of objects
        """
        dic_list = []
        if list_objs is not None:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
        with open(cls.__name__+".csv", "w", newline="") as fi:
            key_list = list(dic_list[0].keys())
            file_csv = csv.DictWriter(fi, fieldnames=key_list)
            file_csv.writeheader()
            for dic in dic_list:
                file_csv.writerow(dic)

    @classmethod
    def create(cls, **dictionary):
        """ class method that create new instance with dictionary
            provided in argument
            Parameters:
                dictionary: dictionary of key, value of new instance
            Returns:
                new instance
        """
        if cls.__name__ == "Rectangle":
            new_ins = cls(2,4)
        else:
            new_ins = cls(3)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """ class method that return list of instance get off file
            Returns:
                list of instance
        """
        try:
            with open(cls.__name__+".json", "r", encoding="utf-8") as fi:
                dic_string = fi.read()
                dic_list = cls.from_json_string(dic_string)
                ins_list = []
                for dic in dic_list:
                    ins_list.append(cls.create(**dic))
                return ins_list
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """ class method that read csv file and get list of
            instance in it
            Return:
                list of instance
        """
        try:
            with open(cls.__name__+".csv", "r", newline="") as fi:
                file_csv = csv.reader(fi)
                key_list = next(file_csv)
                ins_list = []
                for row in file_csv:
                    dic = {}
                    for key, value in zip(key_list, row):
                        dic[key] = int(value)
                    ins_list.append(cls.create(**dic))
                return ins_list
        except FileNotFoundError:
            return []
