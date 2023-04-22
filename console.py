#!/usr/bin/python3
""" a module for the command intepreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A console for AirBNB website clone """

    prompt = 'hbnb'

    def emptyline(self):
        """ implements empty line + enter, to execute nothing """
        pass

    def help_help(self):
        print('provindes infmation to the given command \n help [command]')

    def do_quit(self, line):
        """ Quit commsnd to exit the commnd interpreter """
        return True

    def do_EOF(self, line):
        """ implements the End_of_file attribute """
        if line == 'quit':
            return True
        else:
            return True

    if __name__ == '__main__':
        HBNBCOmmand().cmdloop()
