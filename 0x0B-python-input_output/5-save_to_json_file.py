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
    obj_json = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(obj_json)
