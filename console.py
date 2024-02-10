#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """My class"""
    intro = "Welcome to our AirBnB Console. Type 'help' for commands\n"
    prompt = "(hbnb) "


    def do_EOF(self, args):
        """Signifies end-of-file"""
        return True
    def do_quit(self, args):
        """Quits the program"""
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
