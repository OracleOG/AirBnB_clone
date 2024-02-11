#!/usr/bin/python3

"""
a module that test the cmd module features of python.

contains the console for the first part of the Airbnb Clone project
"""
import cmd


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
