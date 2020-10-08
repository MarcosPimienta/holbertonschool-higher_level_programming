#!/usr/bin/python3
"""Appending text"""


def append_write(filename="", text=""):
    """Appending text"""

    with open(filename, mode='a', encoding="UTF-8") as file:
        return (file.write(text))
