#!/usr/bin/python3

"""
HBNB Console Module

This module defines a custom console class, HBNBCommand, for the AirBnB application.

Attributes:
    prompt (str): Custom prompt for the console.

Methods:
    do_quit(self, args): Quits the program.
    do_EOF(self, args): Handles end-of-file event.

Usage:
    Execute this script to start the AirBnB console. Type 'help' for available commands.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Our custom console class"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quits the program"""
        return True

    def do_EOF(self, args):
        """Signifies end-of-file"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()