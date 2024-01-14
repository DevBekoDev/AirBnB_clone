#!/usr/bin/python3
"""
serializes instances to a JSON file
and
deserializes JSON file to instances
"""


import json
from json.decoder import JSONDecodeError
from datetime import datetime
import sys
import os
import models
sys.path.append('/root/AirBnB_clone/')


class FileStorage:
    """
    class to handle serializes instances to a JSON file
    and
    deserializes JSON file to instances
    """

    __objects = {}
    __file_path = 'file.json'

    def __init__(self):
        """
        constructor
        """
        pass

    def all(self):
        """
        returns objects stored
        """

        return self.__objects

    def new(self, obj):
        """
        sets objects
        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj)] = obj

    def save(self):
        """
        serializes objects and store in json file
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
    
    def reload(self):
        """
        deserializing json file to objects
        """

        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.loads(f.read())
                for value in data_dict.values():
                    cls_name = value.get("__class__")
                    if cls_name:
                        cls = eval(cls_name)
                        instance = cls(**value)
                        self.new(instance)
        except Exception as e:
            pass
