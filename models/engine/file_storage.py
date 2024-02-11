#!/usr/bin/python3

""" a module that test the serialisation => deserialisaton features of python.

contains the class FileStorage that controls the
serialisation => deserialisation process
"""
import json


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
        Attr: __file_path, __objects
        Args: all, new, save, reload
"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        save_dict = {}
        for key, value in self.all().items():
            save_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(save_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.state import State
        class_map = {"BaseModel": BaseModel,
                     "User": User,
                     "Place": Place,
                     "Amenity": Amenity,
                     "City": City,
                     "Review": Review,
                     "State": State}
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                load_dict = json.load(file)

            for key, value in load_dict.items():
                id_key = key.split('.')
                if len(id_key) == 2:
                    class_name, class_id = id_key
                    class_obj = class_map[class_name]
                    if class_obj:
                        class_inst = class_obj(**value)
                        self.new(class_inst)

        except FileNotFoundError:
            pass
