#!/usr/bin/python3
"""
Defines a function that returns an object
represented by JSON string
"""
import json


def from_json_string(my_obj):
    """Returns an object represented by JSON string
    Args:
        my_str: json string
    Return:
        object data
    """
    return json.loads(my_obj)
