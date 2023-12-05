#!/usr/bin/python3
"""This module contains the base class of the project.
It defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class defines all common attributes
    /methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes Public instance attributes:
        id: string - assign with an uuid when an instance is created:
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime
        it will be updated every time you change your object
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
