from importlib.metadata import metadata
import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None
    
    @property
    def body(self):
        return self.data["content"]


    @classmethod
    def load(self, cls, string):

        _, fm, content = self.__regex.split(string, 2)    
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        content["content"] = self.data

    @type.setter
    def type(self, type):
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)
        

