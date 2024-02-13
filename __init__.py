#!/usr/bin/python3
import json

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"  
    __objects = {}  

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        Otherwise, do nothing.
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    
        except FileNotFoundError:
            pass 

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

from models import storage

class BaseModel:

    def save(self):
        """Call save(self) method of storage."""
        storage.save()

    def __init__(self, *args, **kwargs):
        """If it’s a new instance (not from a dictionary representation),
        add a call to the method new(self) on storage.
        """
        if not kwargs:
            storage.new(self)
