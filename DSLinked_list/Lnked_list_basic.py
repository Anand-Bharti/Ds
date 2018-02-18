from user_defined_lib.linked_list_lib import Node

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node



linkedlist = LinkedList(Node(data=10))
linkedlist.insert(20)
pass

