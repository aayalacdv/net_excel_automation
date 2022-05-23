
from enum import Enum, auto

from node import Node


class LinkType(Enum): 
    SLITTER = auto()
    SPLICE = auto()
    SPLITTER = auto()
    RESERVED = auto()

class FiberLink: 

    def __init__(self, incoming  , node : Node, outgoing=None) -> None:
        self.incoming_cable = incoming 
        self.outgoin_cable = outgoing
        self.link_type = self.classify_link(node=node) 


    def classify_link(self, node: Node) -> LinkType: 
        if self.incoming_cable == None: 
            return LinkType.SPLITTER
            
        if self.outgoin_cable == None: 
            
            if node.splitters == None: 
                return LinkType.RESERVED

            return LinkType.SPLITTER
        
        if self.incoming_cable.size != self.outgoin_cable.size: 
            return LinkType.SPLICE
        
        return LinkType.SLITTER



