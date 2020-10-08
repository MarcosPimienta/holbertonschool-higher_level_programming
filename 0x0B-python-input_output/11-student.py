#!/usr/bin/python3
"""Dictionary"""


class Student(object):
    def to_json(self):
        return (self.__dict__)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
