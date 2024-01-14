#!/usr/bin/python3
"""
Base Model For Airbnb
"""

from uuid import uuid4
from datetime import datetime
import sys
import models
from models.engine.file_storage import FileStorage
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

    def to_dict(self):
        """
        return a dictionary keys and values of __dict__
        """

        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp
