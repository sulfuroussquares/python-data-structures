# Hash Tables work by storing key:value pairs of associated data. In python this is known as a 'dictionary'

new dict = {
  "A" : 1,
  "B" : 2,
  "C" : 3
}

# The key has a 'hash function' applied to it, which results in a memory location somewhere that contains the value for that key

# This is one way to implement a hash function
# In Python, ord() returns the unicode for whatever is passed to it
# Here, we are passing in a key value, and for all the characters in that key we are converting them to the unicode equivalent, and then returning that, modulo 100. Value goes in. Transformed value comes out. 

def get_hash(key):
  h = 0
  for char in key:
    h += ord(char)
  return h % 100

class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr= [None for i in range self.MAX]
    # Initializing an array of size 100, and storing no values in each of those array spaces
    # (The syntax here is a 'list comprehension' in Python)



# Sometimes a hash function is applied to two distinct keys but points to the same memory location. When this happens this is called a 'collision'

# One way we can avoid this is by 'chaining'. What this means is that instead of a key being combined with a hash function to point to a memory location for the value, the key is combined with a hash function which points to a linked list.

# Another way to deal with collisions is by 'linear probing'. In this case, if there's a collision, we find the next available memory location (linearly searching for it), and place that value there.

