#!/usr/bin/python3
"""console.py that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class is entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """This method implements exit from the program"""
        return True

    def do_EOF(self, arg):
        """This method handles EOF and exits the program"""
        return True

    def emptyline(self):
        """This method handles an empty line into the program
        It should do nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
