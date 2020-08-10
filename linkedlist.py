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

  def insert_at_end(self, data):
    # edge case: the linked list is empty
    if (self.head is None):
      self.head = Node(data)
      return
    
    # iterate through linked list
    itr = self.head
    
    # this while loop will escape when it reaches the last element
    while (itr.next):
      itr = itr.next

    itr.next = Node(data)




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
    # edge case: the linked list is empty
    if (self.head is None):
      return

    itr = self.head
    # edge case: the first value is the element we want to remove_by_value
    if (itr.data == data_to_remove):
      self.head = itr.next
      return
        
    while (itr.next != data_to_remove):
        # at this point, we're just before the element we want to remove
        itr = itr.next
    itr.next = itr.next.next # connect the chain around the value we remove


# -----------------------------------------------------#
# COMMON CHALLENGES
#------------------------------------------------------#

# Create a deleteNode() function that will take in as inputs, a head node and a position. The function will then delete the node at a given position

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(head, position):
    # while there is a next item to move to, move through array
    itr = head
    idx = 0


    while (itr):
        if (position == 0):
            return head.next

        if (idx == position-1):
            itr.next = itr.next.next
            return head
        itr = itr.next
        idx += 1

# Create a insertNodeAtPosition() function that will take in as inputs, a head node, data, and a position. The function will then insert the data at the specified position.

def insertNodeAtPosition(head, data, position):

    # edge case: the list is empty
    if (head.data is None):
        head.data = data
        return head

    
    
    # traverse the linked list
    itr = head
    idx = 0
    while (itr):
        itr = itr.next
        idx += 1
        if (idx == position - 1):
            temp = itr.next
            itr.next = SinglyLinkedListNode(data)
            itr.next.next = temp
            return head
    
  # This method will take in the head of a linked list, then print the reverse of that linked list (non-recursively)
  def reversePrint(head):
    # recall that a linked list is just a collection of nodes with pointers connecting them

    # so if we were to have the pointers reversing direction (tail becomes the head), we have reversed the linked list

    def reversePrint(head):
    prev = None
    curr = head
    nxt = None

    while (curr):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev

    while(head):
        print(head.data)
        head = head.next
        
  # This method will take in the head nodes of two linked lists and compare the two linked lists.
  # If they are equal in content (all nodes are the same) and in length, it will return 1, otherwise it will return 0

  def compare_lists(llist1, llist2):
    # assuming the linked lists are equal until proven otherwise
    flag = 1

    # checking to see that the lists have equal values within them
    while (llist1 and llist2 ):
        if (llist1.data == llist2.data):
            llist1 = llist1.next
            llist2 = llist2.next
            continue
        # if we are here, it means there are nodes that are not equal
        flag = 0
        break
    # checking to see that the lists are not equal length
    if ((llist1 is None and llist2) or (llist1 and llist2 is None)):
        flag = 0

    return flag

    # this function will, given a head node and a position some distance from the tail, return the value of the node at that position
    def getNode(head, positionFromTail):
    # initialize a data structure to hold values while we pass through the linked list
    # in this case, I'll use a list
    temp = []

    # pass through the linked list, collecting values
    itr = head
    while (itr):
        temp.append(itr.data)
        itr = itr.next

    # retrieve the item at positionFromTail
    retrieved_value = temp[-1*(positionFromTail + 1)]
    return retrieved_value




        


