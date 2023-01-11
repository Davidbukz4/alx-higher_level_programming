#!/usr/bin/python3
"""
Defines a function that add arguments and save it to a file
"""
import sys
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# check if json file is created
if os.path.exists('add_item.json'):
    # if, load from json file to python object and append args
    my_list = list(load_from_json_file('add_item.json'))
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    # convert to json str and save to json file
    save_to_json_file(my_list, 'add_item.json')
else:
    # if not created, create python object and append args
    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    # finally, convert to json str and save to json file
    save_to_json_file(my_list, 'add_item.json')
