#!/usr/bin/python3
"""
   Base class for the project. 
   This class defines all common attributes/methods for other classes:
"""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class in the AirBnB cvonsole project
    
    Attributes :
             id (str): unique user identity
             created_at: instantiated date(time) 
             updated_at: update date (time)
    Methods:
           __init__: class constructor method
           __str__:  prints the class name,id and creates a dictionary
           save: updates instance attributes with given value
           to_dict : returns the dictionary values of an instance obj

    """


    def __init__(self, *args, **kwargs):
        """
        public instance attributes.

        Args:
            *args(args):arguments
            **kwargs(dict):attribute values

        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """Returns sring representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ 
        updates the instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()


    def to_dict(self):
        """ Returns a dictonary containing key-value pairs of 
        the __dict__instance 
        """
        objects = dict()
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                objects[key] = value.isoformat()
            else:
                objects[key] = value
        objects["__class__"] = self.__class__.__name__
        return objects





