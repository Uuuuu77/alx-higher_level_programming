#!/usr/bin/python3
"""
   Module of pascal triangle
"""


def pascal_triangle(n):
    """
       Returns list of lists of integers,
       representing the pascal's triangle(n)
    """
    if n <= 0:
        return []
    my_list = [[1]]
    for x in range(n-1):
        n_list = []
        for y in range(len(my_list[x])+1):
            n_list.extend([([0]+my_list[x]+[0])[y]+([0]+my_list[x]+[0])[y+1]])
        my_list.append(n_list)
    return my_list
