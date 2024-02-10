#!/usr/bin/python3

"""
HBNB Console Module

This module defines a custom console class, HBNBCommand, for the AirBnB application.

Attributes:
    prompt (str): Custom prompt for the console.

Methods:
    do_quit(self, args): Quits the program.
    do_EOF(self, args): Quits the program.

Usage:
    Execute this script to start the AirBnB console. Type 'help' for available commands.
"""

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
    
    def emptyline(self):
        """Called when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()