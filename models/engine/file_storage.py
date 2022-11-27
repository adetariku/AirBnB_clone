#!/usr/bin/python3
"""
Module file_storage for serializing and
deserializing JSON types
"""

import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns a dictionary representation of objects
        """
        return self.__objects

    def new(self, object):
        """sets n __objects the object obj with the key
        <object class name>.id

        Args:
            object(obj): object to write
        """
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({key: value.to_dict() for key, value in self.__objects.items()
                       }, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
