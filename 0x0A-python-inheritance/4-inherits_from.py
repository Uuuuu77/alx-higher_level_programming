#!/usr/bin/python3
"""
   Module of function that test a subclass
"""


def inherits_from(obj, a_class):
    """
       Checks if an object is a subclass of specified class
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
