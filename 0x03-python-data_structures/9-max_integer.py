#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    _max = sorted(my_list)[-1]
    return _max
