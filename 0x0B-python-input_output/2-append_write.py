#!/usr/bin/python3
"""Adds text to EOF"""


def append_write(filename="", text=""):
    """appends to EOF"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
