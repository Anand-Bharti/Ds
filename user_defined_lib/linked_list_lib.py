class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_Node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_Node

    def set_next(self, new_next):
        self.next_Node = new_next


