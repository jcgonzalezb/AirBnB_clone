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
        print(line)
        sto_object = storage.all() 
        line_split = line.split(' ')
        flag = True

        print("sto_object{}".format(sto_object))
        print("line split - {}".format(line_split))
        print("line split [1]- {}".format(line_split[1]))
        if len(line_split) == 0:
            print('** class name missing **')
            return
        elif len(line_split) == 1:
            print('** instance id missing **')
            return
        elif len(line_split) > 0:
            for value in sto_object.values():
                if value.id == line_split[1]:
                    print(value)
            if flag is True:
                print('** no instance found **')
                return
        else:
            instance = eval(line)()
            instance.__str__()
            print(instance)
        #elif line_split not in HBNBCommand.classes:
            #print('** class doesn\'t exist **')
            #return
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
