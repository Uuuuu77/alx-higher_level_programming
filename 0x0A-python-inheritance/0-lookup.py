#!/usr/bin/python3
"""
   Module which has lookup function for listing objects and attributes
"""


def lookup(obj):
    """
       Returns list available attributes and methods of an object
    """
    return dir(obj)
