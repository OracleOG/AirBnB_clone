#!/usr/bin/python3

"""
a module that test the cmd module features of python.

contains the console for the first part of the Airbnb Clone project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """contains entry point of the
      command interpreter for the Airbnb console"""
    prompt = '(hbnb) '


    def do_quit(self, line):
        """command exits the console. (works like EOF)"""
        return True

    def do_EOF(self, line):
        """command exits the console"""
        return True

    def default(self, line):
        """handles instances where an empty line + ENTER is inputed"""
        if not line:
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
