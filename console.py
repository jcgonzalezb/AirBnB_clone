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
        line_split = line.split(' ')
        i = line.split()
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

        sto_object = storage.all()
        key = i[0] + '.' + i[1]
        if key not in sto_object.keys():
            print('** no instance found **')
            return

        else:
            del storage.all()[key]
            storage.save()
            return

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        line_split = line.split(' ')
        string_ins = []
        sto_object = storage.all()

        if line_split[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return

        else:
            for value in sto_object.values():
                string_ins.append(value.__str__())
            print("{}".format(string_ins))

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        line_split = line.split(' ')
        i = line.split()
        sto_object = storage.all()
        key = i[0] + '.' + i[1]
        print(type(line))

        if len(line) == 0:
            print('** class name missing **')
            return

        elif line_split[0] not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
            return

        elif len(line_split) == 1:
            print('** instance id missing **')
            return

        elif key not in sto_object.keys():
            print('** no instance found **')
            return
        
        elif len(line_split) == 2:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print('** attribute name missing **')

        elif len(line_split) == 3:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print('** value missing **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
