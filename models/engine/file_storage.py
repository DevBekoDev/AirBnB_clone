#!/usr/bin/python3
"""
serializes instances to a JSON file
and
deserializes JSON file to instances
"""


from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    """
    class to handle serializes instances to a JSON file
    and
    deserializes JSON file to instances
    """

    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """
        returns objects stored
        """

        return FileStorage.__objects

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
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
