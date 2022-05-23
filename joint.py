from dataclasses import dataclass


@dataclass
class JointBox: 

    def __init__(self, code, id) -> None:
        self.id = id
        self.code = code
        

