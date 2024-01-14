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
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        serializes objects and store in json file
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

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
