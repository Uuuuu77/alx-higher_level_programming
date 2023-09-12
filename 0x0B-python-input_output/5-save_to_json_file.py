#!/usr/bin/python3
"""
   Module of JSON conversion
"""
import json


def save_to_json_file(my_obj, filename):
    """
       Writes an object to text file, using JSON representation
    """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
