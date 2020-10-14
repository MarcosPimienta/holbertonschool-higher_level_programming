#!/usr/bin/python3
"""Base class for test"""
import json


class Base():
    """Base class for test"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Doc for constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Doc for constructor"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Doc for constructor"""
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([i.to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding="UTF-8") as file:
            file.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Doc for constructor"""
        if not json_string:
            jstr = []
            return jstr
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class square rectangle create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 3)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class Load"""
        jstr = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding="UTF-8") as file:
                jstr = cls.from_json_string(file.read())
                return [cls.create(**i) for i in jstr]
        except:
                return jstr

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Doc for constructor"""
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([i.to_dictionary() for i in list_objs])
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding="UTF-8") as file:
            file.write(jstr)

    @classmethod
    def load_from_file_csv(cls):
        """Class Load"""
        jstr = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding="UTF-8") as file:
                jstr = cls.from_json_string(file.read())
                return [cls.create(**i) for i in jstr]
        except:
                return jstr
