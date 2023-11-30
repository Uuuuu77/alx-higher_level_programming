#!/usr/bin/python3
"""
    Module to find peak elements of an array.
"""


def find_peak(list_of_integers):
    """ Finds the peak elements of a list """
    if not list_of_integers:
        return

    begg = 0
    end = len(list_of_integers) - 1

    while begg < end:
        mid = (begg + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            begg = mid + 1
    return list_of_integers[begg]
