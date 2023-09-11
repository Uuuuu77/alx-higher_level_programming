#!/usr/bin/python3
"""
   Module of a class that inherits a list
"""


class MyList(list):
    """
       A class that inherits class list
    """
    def print_sorted(self):
        """
           Prints list in ascending sort
        """
        print(sorted(self))
