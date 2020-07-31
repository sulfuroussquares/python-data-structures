# imports
from linkedlist import Node, LinkedList

# Test Area

if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(1)
  ll.insert_at_beginning(2)
  ll.insert_at_beginning(3)
  ll.print()
  print("created a linked list 3, 2, 1")
  ll.insert_after_value(2,4)
  ll.print()
  print("inserted value 4 after value 2")
  ll.remove_by_value(3)
  ll.print()
  print("removed value 3")
  
