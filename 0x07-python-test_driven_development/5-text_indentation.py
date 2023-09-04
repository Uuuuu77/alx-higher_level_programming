#!/usr/bin/python3
"""
  Indentation of String
"""


def text_indentation(text):
    """
      Prints text with two new lines after each character: . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text1 = ""
    for x in text:
        if x in ['.', ':', '?']:
            text1 += x
            text1 += '\n\n'
        else:
            text1 += x
    text2 = ""
    for y, z in enumerate(text1):
        if z == ' ' and (text1[y-1] in ['\n', ' ']):
            continue
        if (y+1) < len(text1):
            if z == ' ' and (text1[y+1] in [' ']):
                continue
        if z == ' ' and (y == len(text1)-1):
            continue
        text2 += z

    return print(text2, end='')
