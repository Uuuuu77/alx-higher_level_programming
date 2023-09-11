#!/usr/bin/python3
"""
   Module of function that test an instance
"""


def is_same_class(obj, a_class):
    """
       Checks if object is exactly as instance of specified class
    """
    return type(obj) == a_class
