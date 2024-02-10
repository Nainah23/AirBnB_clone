#!/usr/bin/python3
"""Module for HBNB command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Prints help for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def help_EOF(self):
        """Prints help for EOF command"""
        print("EOF command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
