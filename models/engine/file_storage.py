#!/usr/bin/python3
"""a module that serializes & deserialises instances  to json files and back"""
import os
import json


class FileStorage:
    __file_path = 'json_string_file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes te __object to json file"""
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', "encoding=utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """ deserializes the json file to __objects """

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key,value in data.items():
                    self.new(data[__class__](**value))
