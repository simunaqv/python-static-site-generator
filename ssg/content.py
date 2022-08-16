from importlib.metadata import metadata
import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classproperty
    
    def load(self, cls, string):

        _, fm, content = self.__regex.split(string, 2)    
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        content["content"] = self.data


        

