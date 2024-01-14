#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User


def parse(arg):
    return [i.strip(",") for i in split(arg)]

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to e:wqxit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the prgram."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argtemp = parse(arg)
        if len(argtemp) == 0:
            print("** class name missing **")
        elif argtemp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argtemp[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argtemp = parse(arg)
        objdict = storage.all()
        if len(argtemp) == 0:
            print("** class name missing **")
        elif argtemp[0] not in HBNBCommand.__classes:
            print("{}".format(argtemp[0]))
            print("** class doesn't exist **")
        elif len(argtemp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argtemp[0], argtemp[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argtemp[0], argtemp[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        objdict = storage.all()
        argtemp = parse(arg)
        if len(argtemp) == 0:
            print("** class name missing **")
        elif argtemp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argtemp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argtemp[0], argtemp[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argtemp[0], argtemp[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argtemp = parse(arg)
        if len(argtemp) > 0 and argtemp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argtemp) > 0 and argtemp[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argtemp) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        objdict = storage.all()
        argtemp = parse(arg)

        if len(argtemp) == 0:
            print("** class name missing **")
            return False
        if argtemp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argtemp) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argtemp[0], argtemp[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argtemp) == 2:
            print("** attribute name missing **")
            return False
        if len(argtemp) == 3:
            try:
                type(eval(argtemp[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argtemp) == 4:
            obj = objdict["{}.{}".format(argtemp[0], argtemp[1])]
            if argtemp[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argtemp[2]])
                obj.__dict__[argtemp[2]] = valtype(argtemp[3])
            else:
                obj.__dict__[argtemp[2]] = argtemp[3]
        elif type(eval(argtemp[2])) == dict:
            obj = objdict["{}.{}".format(argtemp[0], argtemp[1])]
            for k, v in eval(argtemp[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
