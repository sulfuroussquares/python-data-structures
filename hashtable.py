# # Hash Tables work by storing key:value pairs of associated data. In python this is known as a 'dictionary'.

new_dict = {
  "A" : 1,
  "B" : 2,
  "C" : 3
}

# Although this data structure is built-in in Python, I will code an implementation of it to further familiarize myself with the concepts

# The key has a 'hash function' applied to it, which results in a memory location somewhere that contains the value for that key

# This is one way to implement a hash function
# In Python, ord() returns the unicode for whatever is passed to it
# Here, we are passing in a key value, and for all the characters in that key we are converting them to the unicode equivalent, and then returning that, modulo 100. Value goes in. Transformed value comes out. 

def get_hash(key):
  h = 0
  for char in key:
    h += ord(char)
  return h % 100

# # Here we demonstrate the actual data structure and implement the method defined above

class HashTable:
#   # Basic, Non-Collision-Handling version
#   # def __init__(self):
#   #   self.MAX = 100
#   #   self.arr= [None for i in range(self.MAX)]
#   #   # Initializing an array of size 100, and storing no values in each of those array spaces
#   #   # (The syntax here is a 'list comprehension' in Python)

  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % 10

  def __getitem__(self, key):
    # We need the hash from the given key
    hashed = self.get_hash(key)
    return self.arr[hashed]

  def __setitem__(self, key, value):
    hashed = self.get_hash(key)
    # Assign the object's array at position [key] equal to value
    self.arr[hashed] = value


    # If they key we want to pass in already exists, update it
    # * enumerate() allows us to add a counter while iterating in python
    for index, element in enumerate(self.arr[hashed]):
      if (len(element) == 2 and element[0]== key):
        self.arr[hashed][index] = (key, value)
        found = True
      if not found:
        self.arr[hashed].append((key, value))

    # Assuming the key being used doesn't already exist in our hash map
    # * append() only takes one argument so we're passing in a tuple
    self.arr[hashed].append((key, value))

  # deleting items
  def __delitem__(self, key):
    hashed = self.get_hash(key)
    self.arr[hashed] = None



# # Sometimes a hash function is applied to two distinct keys but points to the same memory location. When this happens this is called a 'collision'

# # One way we can avoid this is by 'chaining'. What this means is that instead of a key being combined with a hash function to point to a memory location for the value, the key is combined with a hash function which points to a linked list.

# # Another way to deal with collisions is by 'linear probing'. In this case, if there's a collision, we find the next available memory location (linearly searching for it), and place that value there.