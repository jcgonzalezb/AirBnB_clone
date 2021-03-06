#!/usr/bin/python3
"""Command line"""


import cmd
from shlex import split
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand defines the command interpreter."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    instance = []

    def do_quit(self, line):
        """Command to exit the program."""
        return True

    def do_EOF(self, line):
        """Command to exit the program."""
        return True

    def emptyline(self):
        """will pass an empty line"""
        pass

    def do_create(self, line):
        """Create an instance."""

        if len(line) == 0:
            print("** class name missing **")

        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Show id and classname of instance."""

        sto_object = storage.all()
        line_split = line.split(" ")
        i = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line_split[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(line_split) == 1:
            print("** instance id missing **")
            return

        sto_object = storage.all()
        key = i[0] + "." + i[1]
        if key not in sto_object.keys():
            print("** no instance found **")
            return

        else:
            print(sto_object[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""

        line_split = line.split(" ")
        i = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line_split[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(line_split) == 1:
            print("** instance id missing **")
            return

        sto_object = storage.all()
        key = i[0] + "." + i[1]
        if key not in sto_object.keys():
            print("** no instance found **")
            return

        else:
            del storage.all()[key]
            storage.save()
            return

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""

        line_split = line.split(" ") if type(line) == str else line
        string_ins = []
        sto_object = storage.all()
        if line:
            if line_split[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            else:
                for value in sto_object.values():
                    string_ins.append(value.__str__())
                print("{}".format(string_ins))

        string_ins = [str(value) for value in sto_object.values()]
        print(string_ins)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""

        line_split = shlex.split(line)
        i = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line_split[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(line_split) == 1:
            print("** instance id missing **")
            return

        sto_object = storage.all()
        key = i[0] + "." + i[1]
        if key not in sto_object.keys():
            print("** no instance found **")
            return

        elif len(line_split) == 2:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print("** attribute name missing **")
                    return

        elif len(line_split) == 3:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print("** value missing **")
                    return

        else:
            setattr(sto_object[key], line_split[2], line_split[3])
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
