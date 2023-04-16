#!/usr/bin/python3
""" a module that defines all the common attributes/methods for other classes
"""

import uuid
from datetime import datetime

class BaseModel:
    """ defines a common attributes/methods in the Airbnb project.
"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    def __str__(self):
        """ Returns the string representation of the Basemodel class """
        return f"[{self.__class__.__name__}] ({ self.id}) {str(self.__dict__)}"

    def save(self):
        """ updates the attribute "save as" with the current datestamp """

        self.updated_at = datetime.today()

    def to_dict(self):
        """ return the dictionary representation of the
instance it represents """

        inst_dict = {'__class__': self.__class__.__name__}

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                inst_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not value:
                    pass
                else:
                    inst_dict.update({key:value})

        return inst_dict
