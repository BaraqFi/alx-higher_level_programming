#!/usr/bin/python3
"""Saves a JSON object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves my_0bj to filename"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
