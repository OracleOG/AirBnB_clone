#!/usr/bin/python3

""" a module that test the cmd module features of python.

contains the class Basemodel where all base attributes of the project is created from
"""
import uuid
from datetime import datetime

class BaseModel:
    """Defines all the common attributes/methods for other classes

    Attr: id, created_at, updated_at
    ARGS: save, to_dict
    """
    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = ((datetime.now()).strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.updated_at = (datetime.now()).strftime("%Y-%m-%dT%H:%M:%S.%f")


    def __str__(self):
        """returns a formated string reprentation of the object"""
        class_name = "BaseModel"
        print(f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = (datetime.now()).strftime("%Y-%m-%dT%H:%M:%S.%f")

    
    def to_dict(self):
