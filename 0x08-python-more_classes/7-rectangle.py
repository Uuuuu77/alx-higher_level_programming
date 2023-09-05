#!/usr/bin/python3
"""
   Module of Rectangle Class
"""


class Rectangle:
    """
       Class Rectangle which defines rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
           Return area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
           Return perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        my_str = ""
        for x in range(self.height):
            for y in range(self.width):
                my_str += str(self.print_symbol)
            if x < (self.height - 1):
                my_str += "\n"
        return my_str

    def __repr__(self):
        return f"{__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
