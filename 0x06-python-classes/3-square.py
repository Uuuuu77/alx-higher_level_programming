#!/usr/bin/python3
""" My Class Square """


class Square:
    """ Initializing my Square
    Args:
       __size: private instance attribute size of my Square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate area of Square
        Return: Public area of the Square
        """
        return (self.__size * self.__size)
