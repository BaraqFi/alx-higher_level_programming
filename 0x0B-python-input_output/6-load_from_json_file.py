#!/usr/bin/python3
"""Loads from JSON file"""
import json


def load_from_json_file(filename):
    """Loads from JSON file"""
    with open(filename) as f:
        return json.load(f)
