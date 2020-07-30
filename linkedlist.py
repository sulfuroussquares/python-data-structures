# Implementing Linked Lists
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self):
    self.head = None

  # This method prints the contents of the linked list
  def print(self):
    if (self.head is None):
      print("ERROR: This linked list is empty!")

    itr = self.head
    while(itr):
      print (itr.data)
      itr = itr.next

    # This method finds an element by data value and inserts a given value after that element
  def insert_value_after(self, data_after, data_to_insert):
  # we must first iterate through the structure and find the data represented by "data after"
    itr = self.head
    while (itr):
      if itr == data_after:
        itr.next = Node(data_to_insert, itr.next)
        break
      itr = itr.next

  # This method inserts an element at the beginning of the linked list
  def insert_at_beginning(self, data):
      # make a node element, and the "next" value of that node is the current head
      node = Node(data, self.head)
      self.head = node

    # def insert_after_value(self, data_after, data_to_insert):
        
    # # Search for first occurance of data_after value in linked list
    # while ()
    # # Now insert data_to_insert after data_after node

    # def remove_by_value(self, data):
    # # Remove first node that contains data
        


