from typing import Any
from node import Node

class LinkedList:
    def __init__(self, *args) -> None:
        self.initial_args = args
        self.node_list: list[Node] = []

        for i in self.initial_args:
            new_node = Node(value = i)
            if self.node_list != []:
                new_node.set_pointer(pointed_node = self.node_list[-1])
            else:
                new_node.set_pointer(pointed_node = new_node)
            self.node_list.append(new_node)
            
    def find_node(self, obj:Any) -> Node|None:
            for i in self.node_list:
                if i.get_value() == obj:
                    return i

    def find_successor(self, node:Node) -> Node|None:
        for i in self.node_list:
            if i.get_pointer() == node:
                return i
            
    def insert(self, object:Any) -> None:
        new_node = Node(value = object, 
                        node_pointer = self.node_list[-1])
        self.node_list.append(new_node)

    def remove(self, object_value:Any):
        node = self.find_node(obj = object_value)
        if node != None:
            successor = self.find_successor(node = node)
            if successor != None:
                successor.set_pointer(pointed_node = node.get_pointer())
            self.node_list.remove(node)
        else:
            raise Exception(f"No items with the value '{object_value}'")

    def info(self):
        info_len = len(self.node_list)
        print('----------------LIST INFO----------------\n',
              f'Number of items in the list: {info_len}')