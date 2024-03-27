#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True
    
    def emptyline(self):
        pass

  import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key not in objects:
                print("** no instance found **")
            else:
                print(objects[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key not in objects:
                print("** no instance found **")
            else:
                del objects[obj_key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = arg.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            objects = storage.all()
            obj_key = class_name + "." + obj_id
            if obj_key not in objects:
                print("** no instance found **")
            else:
                obj = objects[obj_key]
                setattr(obj, attr_name, attr_value)
                obj.save()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
