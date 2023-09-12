#!/usr/bin/python3
"""
   Module of class to JSON
"""


def class_to_json(obj):
    """
       Return dictionary descrption for JSON serialization
    """
    return vars(obj)
