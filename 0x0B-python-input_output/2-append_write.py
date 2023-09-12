#!/usr/bin/python3
"""
   Module of file input/output
"""


def append_write(filename="", text=""):
    """
       Appends a string at the end of text file (UTF-8)
       Return number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as my_file:
        return my_file.write(text)
