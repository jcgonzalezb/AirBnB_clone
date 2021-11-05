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

    def do_show(self, line):
        """Show id and classname of instance."""
        sto_object = storage.all()
        line_split = line.split(' ')
        flag = True

        if len(line) == 0:
            print('** class name missing **')
            return
        elif line_split[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return
        elif len(line_split) == 1:
            print('** instance id missing **')
            return
        elif len(line_split) > 0:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print(value)
                    flag = False
            if flag is True:
                print('** no instance found **')
                return
        else:
                instance = eval(line)()
                instance.__str__()
                print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        sto_object = storage.all()
        line_split = line.split(' ')
        flag = True







if __name__ == '__main__':
    HBNBCommand().cmdloop()
