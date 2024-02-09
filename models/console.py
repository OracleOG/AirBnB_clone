#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the console with ctrl+d or ctrl+z"""
        print("")
        return True
    def do_quit(self, line):
        """Exits the console"""
        return True
    def help_quit(self):
        """Gives information on the exit command"""
        print("Quit command: exit the program")
    def emptyline(self):
        """Do nothing"""
        pass
