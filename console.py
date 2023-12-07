import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the hbnb command interpreter"""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is received"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to end the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

