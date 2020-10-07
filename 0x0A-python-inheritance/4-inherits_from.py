#!/usr/bin/python3
"""Returns true if its a subclass"""


def inherits_from(obj, a_class):
    """Returns true if its a subclass"""

    if type(obj) is a_class:
        return (False)
    return (issubclass(type(obj), a_class))
