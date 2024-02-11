#!/usr/bin/python3

""" a module that test the cmd module features of python.

contains the class Basemodel where all base
attributes of the project is created from
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all the common attributes/methods for other classes

    Attr: id, created_at, updated_at, *args, **kwargs
    methods: save, to_dict, __str__
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        """returns a formated string reprentation of the object"""
        class_name = "BaseModel"
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
