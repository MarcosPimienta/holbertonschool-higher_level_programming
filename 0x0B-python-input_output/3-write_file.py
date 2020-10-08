#!/usr/bin/python3
"""Write to file"""


def write_file(filename="", text=""):
    """Write to file"""

    with open(filename, mode='w', encoding="UTF-8") as file:
        return (file.write(text))
