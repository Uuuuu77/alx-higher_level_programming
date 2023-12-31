#!/usr/bin/python3
"""
   Module of JSON conversion
"""
import json


def to_json_string(my_obj):
    """
       Returns JSON representation of object(string)
    """
    return json.dumps(my_obj)
