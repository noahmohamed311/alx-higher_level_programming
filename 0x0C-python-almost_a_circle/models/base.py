#!/usr/bin/python3
"""base class
"""
import json


class Base:
    """
    base class for almost a circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns json representation of a string
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """
         writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        jstring = []
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                jstring = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(jstring))

    @classmethod
    def load_from_file(cls):
        """
        returns a list of istances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                listd = cls.from_json_string(file.read())
                return [cls.create(**i) for i in listd]
        except Exception:
            return []
