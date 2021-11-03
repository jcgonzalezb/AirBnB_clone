#!/usr/bin/python3
"""
Write a class called BaseModel.
"""

import models
import uuid
import datetime
import time


class BaseModel:
    """
    class BaseModel defines all common
    attributes/methods for other classes.
    Methods:
            save(self)
            to_dict(self)
            __str__(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization function.
        If id is not None,
        Attributes:
            id: string - assign with an uuid when an instance is created.
            created_at: datetime - assign with the current datetime
            when an instance is created.
            updated_at: datetime - assign with the current
            datetime when an instance is created and it will
            be updated every time you change your object.
        """
        attributes = ['created_at', 'updated_at', 'id']
                    
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            
        else:    
            if kwargs is not None and not args:
                for key, value in kwargs.items():
                    if key in attributes:
                        setattr(self, key, value)

    def __str__(self):
        """
        Function that prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Dictionary containing all keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__

        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
