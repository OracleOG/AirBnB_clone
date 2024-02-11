#!/usr/bin/python3

""" a module that is part of the Airbnb clone project.

contains the class Review that inherits from BaseModel
"""
from models.task_5 import BaseModel


class Review(BaseModel):
    """
    Inherits from the BaseModel. contains personal information of the user
    Attr: place_id, user_id, text"""
    place_id = ""
    user_id = ""
    text = ""
