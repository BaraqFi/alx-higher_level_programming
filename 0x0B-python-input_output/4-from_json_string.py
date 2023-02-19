#!/usr/bin/python3
"""JAVASCRIPT OBJECT NOTATION"""
import json


def from_json_string(my_str):
    """Convertes string to JSON object"""
    return json.loads(my_str)
