#!/usr/bin/python3
"""
   Module of file input/output
"""


def read_file(filename=""):
    """
       It reads text file (UTF-8) and print to stdout
    """
    with open(filename, encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
