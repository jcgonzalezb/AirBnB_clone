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
        """Create an instance."""
        if len(line) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self,line):
        """Show id and classname of instance."""
        tokens = line.split    
        if len(line) == 0:
            print('** class name missing **')
            return
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(line) == 1:
            print('** instance id missing **')
            return
        elif len(tokens[2]) < 36:
            print('** no instance found **')
            return
        else:
            instance = eval(line)()
            instance.__str__()
            print(instance)
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
