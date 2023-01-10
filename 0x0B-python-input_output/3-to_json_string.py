#!/usr/bin/python3
"""
Defines a function that returns the JSON representation
of an object string
"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object string
    Args:
        my_obj: object
    Return:
        JSON data
    """
    return json.dumps(my_obj)
