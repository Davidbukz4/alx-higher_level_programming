#!/usr/bin/python3
"""
Defines a function that saves object to a file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation
    Args:
        my_obj: object
        filename: file to save object to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
