#!/usr/bin/python3
"""
   Module of class Student
"""


class Student:
    """
       class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
           Retrieves dictionary representation of Student instance
        """
        my_dict = {}
        if type(attrs) is list and (type(s) is str for s in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict[x] = self.__dict__[x]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
           Replaces all attributes of Student instance
        """
        for key in json:
            setattr(self, key, json[key])
