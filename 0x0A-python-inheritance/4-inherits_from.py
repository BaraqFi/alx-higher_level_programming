#!/usr/bin/python3
"""Defines an inherited class"""


def inherits_from(obj, a_class):
    """Returns true or flase"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
