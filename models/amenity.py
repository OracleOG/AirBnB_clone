#!/usr/bin/python3

""" a module that is part of the Airbnb clone project.

contains the class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from the BaseModel. contains personal information of the user
    Attr: name"""
    name = ""
