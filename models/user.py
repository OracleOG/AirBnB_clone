#!/usr/bin/python3

""" a module that is part of the Airbnb clone project.

contains the class User that inherits from BaseModel
"""
from models.task_5 import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel. contains personal information of the user
    Attr: email, password, firstname, last_name"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
