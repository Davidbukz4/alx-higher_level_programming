#!/usr/bin/python3
"""
Defines a function that creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file
    Args:
        filename: file to save object to
    """
    with open(filename) as f:
        obj = f.read()
    return json.loads(obj)
