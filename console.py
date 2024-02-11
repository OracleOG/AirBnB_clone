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

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        map_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "Place": Place,
                    "Amenity": Amenity,
                    "City": City,
                    "Review": Review,
                    "State": State}

        if line:
            if line in (map_dict):
                New_model = map_dict[line]()
                New_model.save()
                print(New_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        class_names = ["BaseModel", "User", "Place", "Amenity", "City",
                       "Review", "State"]

        if line:
            new_line = line.split()
            if len(new_line) == 2:
                class_key = f"{new_line[0]}.{new_line[1]}"
                if new_line[0] not in class_names:
                    print("** class doesn't exist **")
                else:
                    str_repr = storage.all()
                    if class_key in str_repr:
                        print(str_repr[class_key])
                    else:
                        print("** no instance found **")
            elif len(new_line) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        class_names = ["BaseModel", "User", "Place", "Amenity",
                       "City", "Review", "State"]
        if line:
            new_line = line.split()
            if len(new_line) == 2:
                class_key = f"{new_line[0]}.{new_line[1]}"
                if new_line[0] not in class_names:
                    print("** class doesn't exist **")
                else:
                    str_repr = storage.all()
                    if class_key in str_repr:
                        del (str_repr[class_key])
                        storage.save()

                    else:
                        print("** no instance found **")

            elif len(new_line) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name
        \t Example:
        \t $ all BaseModel |or|
        \t $ all"""
        class_names = ["BaseModel", "User", "Place", "Amenity",
                       "City", "Review", "State"]
        str_list = []
        if line:

            if line not in class_names:
                print("** class doesn't exist **")
            else:
                str_repr = storage.all()
                for key, value in str_repr.items():
                    if value.__class__.__name__ == line:
                        str_list.append(str_repr[key].__str__())
                print(str_list)

        else:
            str_repr = storage.all()
            for key, value in str_repr.items():
                str_list.append(value.__str__())
            print(str_list)

    def do_update(self, line):
        """Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file). """
        class_names = ["BaseModel", "User", "Place", "Amenity",
                       "City", "Review", "State"]
        if line:
            new_line = line.split()
            if len(new_line) == 4:
                class_key = f"{new_line[0]}.{new_line[1]}"
                if new_line[0] not in class_names:
                    print("** class doesn't exist **")
                else:

                    str_repr = storage.all()
                    if class_key in str_repr:
                        obj_repr = str_repr[class_key]
                        setattr(obj_repr, new_line[2], new_line[3])
                        storage.save()

                    else:
                        print("** no instance found **")
            elif len(new_line) == 1:
                print("** instance id missing **")
            elif len(new_line) == 2:
                print("** attribute name missing **")
            elif len(new_line) == 3:
                print("** value missing **")
        else:
            print("** class name missing **")

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
