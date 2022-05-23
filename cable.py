from dataclasses import dataclass


@dataclass
class Cable: 
    start = ''
    end = ''

    def __init__(self, code, id, size, len) -> None:
        self.id = id
        self.code = code
        self.size = size 
        self.len = len 
        self.get_cable_ends()

    
    def get_cable_ends(self) -> None: 
        trims = self.code.split('-')
        self.start = trims[2]
        self.end = trims[3]


    def __eq__(self, other): 
        if not isinstance(other, Cable):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id