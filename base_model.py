#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

class BaseModel:
    def __init__(self, id=None, created_at=None):
        self.id = id
        self.created_at = created_at

my_instance = BaseModel(id="123", created_at="2024-02-13T14:30:00")

my_dict = my_instance.to_dict()
print(my_dict)

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        pass
        else:
            pass

recreated_instance = BaseModel(**my_dict)
print(recreated_instance.id)  
print(recreated_instance.created_at)  
