#!/usr/bin/python3

""" a module that is part of the Airbnb clone project.

contains the class Place that inherits from BaseModel
"""
from models.task_5 import BaseModel


class Place(BaseModel):
    """
    Inherits from the BaseModel. contains personal information of the user
    Attr: city_id, user_id, name, description, number_rooms
          number_bathrooms, max_guest, price_by_night, latitude,
          longitude, amenity_ids"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
