#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

import json
import sys

class BaseModel:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"BaseModel {self.id}"

class Controller:
    def __init__(self):
        self.models = {}

    def create(self, args):
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel(id=args[2])
            self.models[model.id] = model
            print(model.id)

    def show(self, args):
        if len(args) < 2:
            print("** class name missing **")
        elif args[1] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 3:
            print("** instance id missing **")
        elif args[2] not in self.models:
            print("** no instance found **")
        else:
            print(str(self.models[args[2]]))


def main():
    controller = Controller()
    while True:
        cmd = input("$ ").split()
        if cmd[0] == "create":
            controller.create(cmd)
        elif cmd[0] == "show":
            controller.show(cmd)      

if __name__ == "__main__":
    main()

class HBNBCommand(cmd.Cmd):
    # ...

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
