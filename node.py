from dataclasses import dataclass

@dataclass
class Node: 

    def __init__(self, id) -> None:
        self.id = id
        self.links = []
        self.splitters = None 
        self.clients = None 


    def add_link(self, link) -> None: 
        self.links.append(link)

    def add_splitters_and_clients(self, clients : int, isSat = False) -> None: 
        self.clients = clients

        if clients > 20: 
            self.splitters = 3
        elif clients > 10 & clients < 20: 
            self.splitters = 2
        if clients < 10: 
            self.splitters = 1
        if isSat: 
            self.splitters = 0


    