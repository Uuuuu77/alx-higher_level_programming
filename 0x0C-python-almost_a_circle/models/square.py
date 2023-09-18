#!/usr/bin/python3
"""
   Models/square.py of Square class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
       Square class inheriting Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Intializing Square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Set property of size """
        return self.width

    @size.setter
    def size(self, value):
        """ Getting value of size """
        self.width = value
        self.height = value

    def __str__(self):
        """ String output """
        return ("[{}] ({}) {}/{} - {}"
                .format(__class__.__name__, self.id, self.x, self.y,
                        self.size))

    def update(self, *args, **kwargs):
        """ Update Square class arguments """
        ar = ['id', 'size', 'x', 'y']
        if not args and kwargs is not None:
            for var, val in kwargs.items():
                if var in ar:
                    setattr(self, var, val)
        for var, val in zip(ar, args):
            setattr(self, var, val)

    def to_dictionary(self):
        """ Returns dictionary of class instance """
        keys = ['size', 'x', 'y', 'id']
        dta = self.__dict__
        dt = {k: v for k, v in dta.items() if not k.endswith('height')}
        dct = dict(zip(keys, list(dt.values())))
        return dct
