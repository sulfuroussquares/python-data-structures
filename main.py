# imports
from linkedlist import Node, LinkedList
from hashtable import HashTable

# Test Area

if __name__ == '__main__':
  t = HashTable()
  t["value 1"] = 1
  t["value 2"] = 2
  print(t.arr)
  del t["value 1"]
  print(t.arr)
