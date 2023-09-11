#!/usr/bin/python3
"""
   Module of Geometry class
"""


class BaseGeometry:
    """
       Parent class of Geometry
    """
    def area(self):
        """
           Calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
           It validates the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
