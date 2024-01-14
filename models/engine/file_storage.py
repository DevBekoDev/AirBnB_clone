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

        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """
        deserializing json file to objects
        """

        try:
            deserialized = {}
            with open(self.__file_path, "r") as f:
                deserialized = json.loads(f.read())
            for key, vlaue in deserialized.items:
                self.__objects[key] = eval(obj["__class__"])(**obj)
        except (FileNotFoundError, JSONDecodeError):
            # Noo error handiling required
            pass
