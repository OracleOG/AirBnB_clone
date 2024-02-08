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
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__Class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self,key, value)

        else:
            #The date and time over here does not need to be cast as string

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            


    def __str__(self):
        """returns a formated string reprentation of the object"""
        class_name = "BaseModel"
        print(f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = (datetime.now()).strftime("%Y-%m-%dT%H:%M:%S.%f")

    
    def to_dict(self):
        """Returns a ditionary of instance attributes"""
        dictionary = dict((key, value) for key, value in self.__dict__.items())
        dictionary['__class__'] = self.__class__

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()


        return dictionary
