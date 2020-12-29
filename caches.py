# We want a struture that will store a set of items, then allow us to reorganize them as we use items, storying the least recently used (LRU) towards the "top" or the "front"

# The list part of this implies a linked list of some sort
# The least recently used part would imply a stack, except that we want to manipulate the structure so that just accessing an element will move it to the top
# a linked list will suffice here
# also, because we are looking to retrieve a particular piece of information, given another piece of information, this implies using a hash map of some sort
# thus, we should use a linked list of hash maps

class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  # mandatory init method
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

  # Inserting items into the linked list
  def insert(self, item):
    # iterate through the list until we find the last element (The one where .next is none)
    if self.head is None:
      head = Node(item)
    
    itr = head
    while (itr.next):
      itr = itr.next
    
    # we got to the last element now
    itr.next = Node(item)


# ----------------------------------------------------

# When a page is referenced, the required page may be in the memory. If it is in the memory, we need to detach the node of the list and bring it to the front of the queue.

# we need a linked list of hash maps
class lru_cache:
  def __init__(self):
    self.head = None

  def add(self, item):
    

# 1. go find the node with the corresponding data




# detach the node and bring it to the front
# given a standard linkedlist this might mean setting the previous element's "next" to the element after the one we want to manipulate, and setting the head to this element.




# If the required page is not in memory, we bring that in memory.
# this just means set the head to that item
