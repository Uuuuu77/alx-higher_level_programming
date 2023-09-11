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
        raise Exception('area() is not implemented')
