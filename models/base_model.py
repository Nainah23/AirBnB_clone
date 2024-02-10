#!/usr/bin/python3
"""Write a class BaseModel"""

from datetime import datetime, timezone
from models import storage
import uuid
import json

class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ initializes the BaseModel object"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

            """Add the new instance to storage"""
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """provides a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute with the current time"""
        self.updated_at = datetime.now(timezone.utc)
        """Save the updated instance to storage"""
        storage.save()

    def to_dict(self):
        """reates a dictionary representation of the object with the necessary format."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
