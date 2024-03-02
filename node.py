from __future__ import annotations
from typing import Any


class Node: 

    _NODE_COUNTER = 0
    
    def __init__(self, value:Any, node_pointer:Node = None) -> None:
        self.id = Node._NODE_COUNTER
        self.value = value
        self.node_pointer = node_pointer

        Node._NODE_COUNTER += 1
    
    def get_id(self):
        return self.id
    
    def get_value(self):
        return self.value
    
    def get_pointer(self):
        return self.node_pointer

    
    def set_value(self,new_value:Any)->None:
        self.value = new_value

    def set_pointer(self,pointed_node: Node)->None:
        self.node_pointer = pointed_node