#!/usr/bin/python3
"""
Instance class FileStorage
"""


import json
import models

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
        """Sets an obj with class name and id"""
        
        self.__objects['{}.{}'.format(type(obj).__name__, obj.id)] = obj
        

    def save(self):
        """Serializes __objects (dict) to the JSON file"""
        dic = {}
        for key, values in self.__objects.items():
            dic[key] = values.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dic, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                read = file.read()
                dic = json.loads(read)
            
            for key, value in dic.items():
                instance = eval(value['__class__'])(**value)
                self.__object[key] = instance
        except:
            pass