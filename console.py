#!/usr/bin/python3
"""Command line"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand defines the command interpreter."""
    prompt = '(hbnb) '
    classes = {"BaseModel"}

    def do_quit(self, line):
        """Command to exit the program."""
        return True

    def do_EOF(self, line):
        """Command to exit the program."""
        return True

    def emptyline(self):
        """will pass an empty line """
        pass

    def do_create(self, line):
        if len(line) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
