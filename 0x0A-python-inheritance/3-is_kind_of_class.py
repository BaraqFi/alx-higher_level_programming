#!/usr/bin/python3
"""Defines kind of class"""


def is_kind_of_class(obj, a_class):
    """Returns true or false"""

    if isinstance(obj, a_class):
        return True
    return False
