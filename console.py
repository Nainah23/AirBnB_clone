#!/usr/bin/python3
"""
console.py
"""

import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """
    Create commande cmd
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quits the program.
        """
        return True

    def do_EOF(self, line):
        """
        Quits the program.
        """
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_help(self, arg):
        """
        help function
        """
        return super().do_help(arg)

    def do_create(self, arg):
        """
        cCreates a new instance of a specified class
        """
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show an instance with ID
        """
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instances = objects.get(key, None)
        if instances is None:
            print("** no instance found **")
            return
        print(instances)

    def do_destroy(self, arg):
        """
        destroy an instance with ID
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        objects = storage.all()

        if len(args) < 1:
            print(["{}".format(v) for _, v in objects.items()])
            return

        class_name = args[0]
        if class_name not in classes.keys():
            print("** class doesn't exist **")
            return

        """Retrieve all instances of the specified class"""
        class_instances = classes[class_name].all()
        print(["{}".format(instance) for instance in class_instances])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        objs = storage.all()
        key = args[0] + "." + args[1]

        if key not in objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = objs[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()

    def do_count(self, arg):
        """count  the number of instances of a given class."""
        argl = arg.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[: match.span()[0]], arg[match.span()[1] :]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][: match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
