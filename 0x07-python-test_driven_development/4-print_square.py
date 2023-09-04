#!/usr/bin/python3
"""
  Print a square
"""


def print_square(size):
    """
      Prints a square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for x in range(size):
            print("#", end="")
        print()
