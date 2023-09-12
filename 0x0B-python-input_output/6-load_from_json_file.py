#!/usr/bin/python3
"""
   Module of JSON conversion
"""
import json


def load_from_json_file(filename):
    """
       Creats an object from a JSON file
    """
    with open(filename) as my_file:
        return json.load(my_file)
