#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    create file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all instances.
        If cls is specified, returns only instances of that class.
        """
        if cls is None:
            return self.__objects
        else:
            instances = {}
            for key, obj in self.__objects.items():
                if type(obj) == cls:
                    instances[key] = obj
            return instances

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(save_obj, fd)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        current_classes = {
            "BaseModel": BaseModel,
            "User": User,
        }

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                dict_objs = json.load(file)
                for key, value in dict_objs.items():
                    cls_name = key.split(".")[0]
                    if cls_name in current_classes:
                        instance = current_classes[cls_name](**value)
                        self.new(instance)
