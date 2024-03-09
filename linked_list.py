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


    # Private methods  
    def __find_node(self, obj:Any) -> Node|None:
        '''
            This function searches and returns a node by its value
        '''
        for i in self.node_list:
            if i.get_value() == obj:
                return i

    def __pointedby(self, node:Node) -> Node|None:
        '''
            This function takes a target node as input and returns the node who point the target
        '''
        for i in self.node_list:
            if i.get_pointer() == node:
                return i
            

    # Public methods
    def insert(self, object:Any) -> None:
        '''
            This function takes a value as input, creates a new node containing 
            the specified value and sets the pointer to the last item of the list 
        '''
        new_node = Node(value = object, 
                        node_pointer = self.node_list[-1])
        
        self.node_list.append(new_node)

    def remove(self, object_value:Any):
        '''
            This function takes the value to be removed from the list as input, checks for nodes
            containing such value and removes the first node found. After deleting the node,
            the function sets the pointer of the successor to the ancestor of the removed node.
        '''
        node = self.__find_node(obj = object_value)
        
        if node != None:    
            successor = self.__pointedby(node = node)
            
            if (successor != None) and (node != self.node_list[0]):
                successor.set_pointer(pointed_node = node.get_pointer())
            elif node != self.node_list[0]:
                successor.set_pointer(pointed_node = successor)
            
            self.node_list.remove(node)
        else:
            raise Exception(f"No items with the value '{object_value}'")

    def info(self):
        info_len = len(self.node_list)
        print('----------------LIST INFO----------------\n',
              f'Number of items in the list: {info_len}')