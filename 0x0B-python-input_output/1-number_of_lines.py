#!/usr/bin/python3
"""Read that file"""


def number_of_lines(filename=""):
    """Read that file"""

    with open(filename, 'r') as file:
        return(sum(1 for line in file))
