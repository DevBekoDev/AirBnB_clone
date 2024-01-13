#!/usr/bin/python3
"""
Base Model For Airbnb
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Start of the basemodel class
    """

    def __init__(self, *args, **kwargs):
        """
        initialize instances
        """

        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for key, value in kwargs.items():
            if key == "__class__":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self._updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        return "[{}] ({}) <{}>".format(
                type(self).__name__, self.id, self.__dict)

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
