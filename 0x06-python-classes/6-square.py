#!/usr/bin/python3
""" My Class Square """


class Square:
    """ Initializing my Square
    Args:
       __size: Private instance attribute size of Square
       __position: Private instance attribute position of Square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculate the area of Square
        Return: The area of Square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ Public method my_print
            that prints to stdout of Square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for b in range(self.__size):
                for c in range(self.position[0]):
                    print(" ", end="")
                for d in range(self.__size):
                    print("#", end='')
                print()
