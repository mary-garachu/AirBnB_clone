#!/usr/bin/python3
"""
This is the console base for the unit
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Defines the hbnb command interpreter"""
    prompt = '(hbnb) '
    my_dict = {'BaseModel': BaseModel}

    def emptyline(self):
        """Do nothing when an empty line is received"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to end the program"""
        return True

    def do_create(self, arg):
        """ Creates a new instance of the basemodel class
        saves it and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.my_dict[my_data[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        save the change into the JSON file
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        cmd_input = shlex.split(arg)
        if len(cmd_input) == 0:
            print("** class name missing **")
            return
        if cmd_input[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(cmd_input) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        obj_dict = storage.all()
        cmd_key = cmd_input[0] + "." + cmd_input[1]
        if cmd_key in obj_dict:
            del obj_dict[cmd_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based on the class name
        """
        storage.reload()
        my_json = []
        objs_dict = storage.all()
        if not arg:
            for key in objs_dict:
                my_json.append(str(objs_dict[key]))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.my_dict.keys():
            for key in objs_dict:
                if token[0] in key:
                    my_json.append(str(objs_dict[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
