#!/usr/bin/python3
"""
   Module has class that inherits int class
"""


class MyInt(int):
    """
       Class inheriting class int
    """
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
