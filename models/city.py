#!/usr/bin/python3

""" a module that is part of the Airbnb clone project.

contains the class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from the BaseModel. contains personal information of the user
    Attr: state_id, name"""
    state_id = ""
    name = ""
