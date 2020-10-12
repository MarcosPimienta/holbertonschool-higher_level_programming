#!/usr/bin/python3
"""Base class for test"""


import json


class Base():
    """Base class for test"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = "[]"
        else:
            return json.dumps(list_dictionaries)
