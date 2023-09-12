#!/usr/bin/python3
"""
   Module to search & update file
"""


def append_after(filename="", search_string="", new_string=""):
    """
       Inserts a line of text to file,
       after each line has a specific string
    """
    with open(filename, encoding="UTF-8") as my_file:
        lines = my_file.readlines()

    with open(filename, 'w', encoding="UTF-8") as my_file:
        for line in lines:
            if search_string in line:
                line += new_string
            my_file.write(line)
