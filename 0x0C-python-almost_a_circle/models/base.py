#!/usr/bin/python3
"""
   Base module of Base class
"""
import json
import csv


class Base:
    """
       Class B ase of all classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
           Initializing Base class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dict):
        """
           Returns the JSON string representation of list_dict
        """
        if list_dict is None or list_dict == []:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """ 
           Writes the JSON string to a file
        """
        file_name = f"{cls.__name__}.json"
        dict_list = []
        if list_objs is not None:
            for objs in list_objs:
                dict_list.append(objs.to_dictionary())
        with open(file_name, mode='w', encoding='UTF-8') as my_file:
            my_file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
           Returns the list of the JSON string representation
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
           Returns instance with all attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
           Returns a list of instances
        """
        file_name = f"{cls.__name__}.json"
        try:
            with open(filename, encoding='UTF-8') as my_file:
                dict_list = cls.from_json_string(my_file.read())
        except IOError:
            return []
        instances = []
        for dct in dict_list:
            instances.append(cls.create(**dct))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
           Serializes class object to CSV
        """
        file_name = f"{cls.__name__}.csv"
        with open(file_name, 'w', newline='') as my_file:
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(my_file, field_names=field_names)
            writer.writeheader()
            for objs in list_objs:
                writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
           Deserializes csv to class object
        """
        file_name = f"{cls.__name__}.csv"
        dict_list = []
        try:
            with open(file_name, newline='') as my_file:
                reader = csv.DictReader(file)
                for row in reader:
                    for var, val in row.items():
                        row[var] = int(val)
                    dict_list.append(row)
        except IOError:
            return []
        instances = []
        for dct in dict_list:
            instances.append(cls.create(**dct))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
           Opens window and draws all the Rectangles and Squares
        """
        s = turtle.Screen()
        t = turtle.Turtle()
        t.speed(2)
        t.pensize(5)
        t.color('blue', 'pink')
        t.penup()
        for rect in list_rectangles:
            t.goto((rect.width + 10), (rect.height + 10))
            t.pendown()
            t.begin_fill()
            for b in range(2):
                t.fd(rect.width)
                t.lt(90)
                t.fd(rect.height)
                t.lt(90)
            t.penup()
            t.end_fill()

        t.color('red', 'green')
        for sq in list_squares:
            t.goto((sq.width - 200), (sq.height - 200))
            t.pendown()
            t.begin_fill()
            for b in range(2):
                t.fd(sq.width)
                t.lt(90)
                t.fd(sq.height)
                t.lt(90)
            t.ht()
            t.penup()
            t.end_fill()
        s.exitonclick()
