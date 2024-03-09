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
    def __find_node(self, object_value:Any) -> Node|None:
        '''
            This function searches and returns a node by its value
        '''
        for i in self.node_list:
            if i.get_value() == object_value:
                return i

    def __pointedby(self, node:Node) -> Node|None:
        '''
            This function takes a target node as input and returns the node who point the target
        '''
        for i in self.node_list:
            if i.get_pointer() == node:
                return i
            

    # Public methods
    def insert(self, object_value:Any) -> None:
        '''
            This function takes a value as input, creates a new node containing 
            the specified value and sets the pointer to the last item of the list 
        '''
        new_node = Node(value = object_value, 
                        node_pointer = self.node_list[-1])
        
        self.node_list.append(new_node)

    def remove(self, object_value:Any) -> None:
        '''
            This function takes the value to be removed from the list as input, checks for nodes
            containing such value and removes the first node found. After deleting the node,
            the function sets the pointer of the successor to the ancestor of the removed node.
        '''
        node = self.__find_node(object_value = object_value)
        
        if node != None:    
            successor = self.__pointedby(node = node)
            
            if (successor != None) and (node != self.node_list[0]):
                successor.set_pointer(pointed_node = node.get_pointer())
            elif node == self.node_list[0]:
                successor.set_pointer(pointed_node = successor)
            
            self.node_list.remove(node)
        else:
            raise Exception(f"No items with the value '{object_value}'")
        
    def insertAt(self, object_value:Any, position_idx: int) -> None:
        '''
            This function takes a value as input, creates a new node containing 
            the specified value and sets the pointer based on the position_idx.
            The position_idx starts from 0.
            You should use this function ony when you want to insert the node 
            at any position inside the list. 
            Use the insert() function to append a node exclusively at the end of the list. 

            Examples:
                                ['item0' <- 'item1' <- 'item2' <- 'item3']
            
            calling insertAt() at position 2 will modify the list in this way:

                            ['item0' <- 'item1' <- 'NEW_ITEM' <- 'item2' <- 'item3']
            
            In the case of position_idx is 0 then the list will be:
                            
                            ['NEW_ITEM' <- 'item0' <- 'item1' <- 'item2' <- 'item3']
            
            and the new node will point to itself.
            Finally, in the case of the position_idx is equal to the last element of the list, the new list will be:

                            ['item0' <- 'item1' <- 'item2' <- 'NEW_ITEM' <- 'item3']

            The position_idx specifies which node in the list the new node will be pointed from.
        '''
        if position_idx <= len(self.node_list)-1:
            # Actual node at the specified position
            actual_node = self.node_list[position_idx]

            new_node = Node(value = object_value)

            if position_idx == 0:
                new_node.set_pointer(pointed_node = new_node)    
            else:
                new_node.set_pointer(pointed_node = actual_node.get_pointer)
            
            # Refresh the acutal_node pointer to the new node
            actual_node.set_pointer(pointed_node = new_node)

            self.node_list.insert(position_idx,new_node)
        else:
            raise Exception(f"The specified position '{position_idx}' exceeds the lenght of the list.")

    def info(self):
        print(' ----------------LIST INFO----------------\n\n',
              f'Number of items in the list: {len(self.node_list)}\n\n',
              '----------------LIST ITEMS----------------\n')
        for i in self.node_list:
            print(f'{i.get_value()}\n')
        