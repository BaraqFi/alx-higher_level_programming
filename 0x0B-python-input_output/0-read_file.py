#!/usr/bin/python3
"""Reads a file in stout"""


def read_file(filename=""):
    """Reads line and prints every line"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
