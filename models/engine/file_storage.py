#!/usr/bin/python3

"""File Storage class serialization 
into JSON files and deserialization 
of JSON files into instances.
"""

import json
from os import path
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        new = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self): 
        """serializes __objects to the JSON file (path: __file_path)"""
        s_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path) as file:
            json.dump(s_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)

