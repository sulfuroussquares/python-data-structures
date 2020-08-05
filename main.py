# imports
from linkedlist import Node, LinkedList
from hashtable import HashTable
from collections import deque
import replit

# Test Area

if __name__ == '__main__':
  
  example = deque()
  example.append('item 1')
  example.append('item 2')
  example.append('item 3')

  example.pop()
  print(example)