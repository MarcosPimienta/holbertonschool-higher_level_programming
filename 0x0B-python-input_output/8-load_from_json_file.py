#!/usr/bin/python3
"""Go for it JSON!!!!"""


import json


def load_from_json_file(filename):
    """Go for it JSON!!!!"""

    with open(filename, mode='r', encoding="UTF-8") as file:
        return json.load(file)
