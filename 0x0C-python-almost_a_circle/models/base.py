#!/usr/bin/python3

""" class Base"""

import json


class Base:
    """Base class for managing instances with an ID attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID for the instance. If None,
            a new ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a JSON file.

        Args:
            list_objs (list): List of instances to be saved.

        Returns:
            None
        """
        if list_objs is None:
            return "[]"
        obj_dict_list = [i.to_dictionary() for i in list_objs]
        json_str = cls.to_json_string(obj_dict_list)
        with open(cls.__name__ + ".json", "w", encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
