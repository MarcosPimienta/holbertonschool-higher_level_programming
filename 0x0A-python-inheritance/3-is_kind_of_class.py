#!/usr/bin/python3
"""Returns true if its the same kind"""


def is_kind_of_class(obj, a_class):
    """Returns true if its the same kind"""

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
