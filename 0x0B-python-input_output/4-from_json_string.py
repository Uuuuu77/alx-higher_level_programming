#!/usr/bin/python3
"""
   Module of JSON conversion
"""
import json


def from_json_string(my_str):
    """
       Returns an object(python datad structure) rep by a JSON string
    """
    return json.loads(my_str)
