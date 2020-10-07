#!/usr/bin/python3
"""Read that file"""


def read_file(filename=""):
    """Read file"""

    with open(filename, 'r+') as file:
        print(file.read())
