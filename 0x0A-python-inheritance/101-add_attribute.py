#!/usr/bin/python3
"""
   Module that set attribute
"""


def add_attribute(ob, key, value):
    """
       Check and sets attribute to object
    """
    if not hasattr(ob, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(ob, key, value)
