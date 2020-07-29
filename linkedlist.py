class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
  class LinkedList:
    def __init__(self):
      self.head = None

    def insert_value_after(self, data_after, data_to_insert):
    # we must first iterate through the structure and find the data represented by "data after"
      itr = self.head
      while (itr):
        if itr == data_after:
          itr.next = Node(data_to_insert, itr.next)
          break
        itr = itr.next
        


