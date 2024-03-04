from datetime import datetime
from uuid import uuid4

class MyBase:

    # updating MyBase class constructor with special parameters
    def __init__(self, *args, **kwargs):
       # discard the __class__ key if dictionary is not empty
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
    # grab date & time stamp keys and convert its values to datetime obj
                if key == "created_at" or key == "updated_at":
                   dtime = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                   setattr(self, key, dtime)
                else:
                    setattr(self, key, val)
        else:
               # create/assign ID, created_at & updated_at (new instance)
             self.id = str(uuid4())
             self.created_at = datetime.now()
             self.updated_at = datetime.now()
    def save_update(self):
          # update the updated_at attribute with the current date & time
        updated_at = datetime.now()

    def save_to_dict(self):
        # returns a dictionary containing all keys/values of __dict__ of 
        # all the instance                       
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat

    def __str__(self):
        # string representation of all class instance and its attributes
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
# creating a class instance and update it with a few attributes
my_model = MyBase()
my_model.name = "Julien Kimba"
my_model.julien_age = 37
print(my_model.id)
print(my_model)
print(my_model.created_at)
print("\n------- Serialized to dictionary below -------\n")
my_model_json = my_model.save_to_dict()
print(my_model_json)
print("\n------ JSON of <'my_model'> below ------\n")
for key, value in my_model_json.items():
    print("\t{}: ({}) - {}".format(key, type(value), value))
print("\n ------ deserialized to an instance below ------\n")
#parse in the dictionary to the class constructor for deserialization 
new_model = MyBase(**my_model_json)
print(new_model.id)
print(new_model)
print(new_model.created_at)
print("\n------ the two instanceses compared below -----\n")
print(new_model is my_model)
