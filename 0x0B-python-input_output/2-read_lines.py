#!/usr/bin/python3
"""Read lines of file"""


def read_lines(filename="", nb_lines=0):
    """Read lines of file"""

    with open(filename, encoding="UTF-8") as file:
        i = 0
        while (True):
            num = file.readline()
            if not num:
                break
            if i < nb_lines or nb_lines <= 0:
                print(num[:-1])
            i += 1
