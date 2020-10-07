#!/usr/bin/python3
"""Read that file"""


def read_file(filename=""):
    """Read file"""

    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
