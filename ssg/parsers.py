from typing import List
from pathlib import Path
class Parser:
    extensions:List[str] = []

    def valida_extension(self, extension):
        found = extension in self.extensions
        return found

    def parse(self, path:Path, source:Path, dest:Path):
        raise NotImplementedError("Not implemented.")

    def read(self, path):
        with path:
            
