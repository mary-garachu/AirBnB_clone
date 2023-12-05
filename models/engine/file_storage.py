#!/usr/bin/python3
"""
This module contains
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from os.path import exists


class FileStorage:
    """
    serializes instances to a JSON file
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, value in self.__objects.items():
            if hasattr(value, 'to_dict') and callable(
                    getattr(value, 'to_dict')):
                serialized_objs[key] = value.to_dict()
            else:
                serialized_objs[key] = value
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise do nothing
        If the file doesn’t exist, no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                print("File is present")
                loaded_objs = json.load(file)
                self.__objects = loaded_objs
        else:
            pass
