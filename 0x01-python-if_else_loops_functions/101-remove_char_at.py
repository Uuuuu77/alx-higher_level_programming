#!/usr/bin/python3
def remove_char_at(str, n):
    rm = len(str)
    if (n >= 0 and n < rm):
        return (str.replace(str[n], ''))
    else:
        return str
