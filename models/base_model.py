#!/usr/bin/python3
"""
Base Model For Airbnb
"""

from uuid import uuid4
from datetime import datetime
import sys
import models
sys.path.append('/root/AirBnB_clone/')


class BaseModel:
    """
    Start of the basemodel class
    """

    def __init__(self, *args, **kwargs):
        """
        initialize instances
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        return "[{}] ({}) <{}>".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        update last updated_at variable
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary keys and values of __dict__
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
