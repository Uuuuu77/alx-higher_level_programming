#!/usr/bin/python3
""" My class Square """


class Square:
    """ Initializing my Square
    Args:
       __size: Private instance attribute size of Square
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
        """ Calculate the area of a Square
        Return: Area of a Square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ Public metho my_print
            which print to stdout the square with character #
        """
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end='')
                print()
