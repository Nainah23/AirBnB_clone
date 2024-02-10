#!/usr/bin/python3

"""
HBNB Console Module

This module defines a custom console class, HBNBCommand, for the AirBnB application.

Attributes:
    prompt (str): Custom prompt for the console.

Methods:
    do_quit(self, args): Quits the program.
    do_EOF(self, args): Quits the program.
    def do_create(self, arg): 
     - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
    def do_show(self, arg):
     - Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
    do_destroy(self, arg):
     - Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
    def do_all(self, arg):
     - Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel 

Usage:
    Execute this script to start the AirBnB console. Type 'help' for available commands.
"""

import cmd
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel": BaseModel}


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

    def do_create(self, arg):
        """
        Creates a new instance of a specified class, saves it (to the JSON file), and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = arg.split()
        objs = storage.all()

        if not arg:
            print([str(objs[key]) for key in objs])
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        print([str(objs[key]) for key in objs if key.startswith(args[0] + ".")])

if __name__ == '__main__':
    HBNBCommand().cmdloop()