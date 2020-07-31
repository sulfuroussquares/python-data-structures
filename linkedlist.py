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

  # This method inserts an element after a particular value, and based on the first instance of that value it finds
  def insert_after_value(self, data_after, data_to_insert):
    # start at the beginning
    itr = self.head 
    while (itr.data != data_after):
      itr = itr.next

    # at this point, we've found the element we want to insert an element after
    temp = itr.next # store the link to the next value
    itr.next = Node(data_to_insert)
    itr.next.next = temp # complete the chain

    # Remove first node that contains data
  def remove_by_value(self, data_to_remove):
    itr = self.head
    # edge case: the first value is the element we want to remove_by_value
    if (itr.data == data_to_remove):
      itr.next = self.head
      
        
    while (itr.next != data_to_remove):
        # at this point, we're just before the element we want to remove
        itr = itr.next
          
    itr.next = itr.next.next # connect the chain around the value we remove


        


