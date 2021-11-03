#!/usr/bin/python3
"""
Instance class FileStorage
"""

import json


class FileStorage:
    """
    That serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets an obj"""
        self.__objects['{}.{}'.format(obj.__class__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects (dict) to the JSON file"""
        dic = {}
        for key, values in self.__objects.items():
            dic[key] = values.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if self.__file_path is not None:
            __objects = json.loads(self.__file_path)
