#!/usr/bin/python3
""" My Class Square """


class Square:
    """ Initializing my Square
    Args:
       __size: private instance attribute size of Square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of Square
        Return: Area of Square
        """
        return (self.__size * self.__size)
