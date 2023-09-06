#!/usr/bin/python3
"""
   Module of LockedClass which prevents creating new attributes
"""


class LockedClass:
    """
      Prevent addition of new attributes
    """
    __slots__ = ["first_name"]
