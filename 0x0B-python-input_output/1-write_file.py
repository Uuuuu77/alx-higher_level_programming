#!/usr/bin/python3
"""
   Module of file input/output
"""


def write_file(filename="", text=""):
    """
       Writes a string to text file (UTF-8)
       Return number of character written
    """
    with open(filename, mode='w', encoding="utf-8") as my_file:
        return my_file.write(text)
