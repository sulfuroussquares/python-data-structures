# Linked Lists in Python

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = nextInt

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # make a node element, and the "next" value of that node is the current head
        node = Node(data, self.head)
        self.head = node

    def insert_after_value(self, data_after, data_to_insert):
        
    # Search for first occurance of data_after value in linked list
    while ()
    # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
    # Remove first node that contains data
