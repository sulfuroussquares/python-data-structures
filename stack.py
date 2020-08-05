# Real-World Use Case for Stacks: Writing a "back" button agnostically on a webpage, so that the program remembers last thing you looked at on a webpage

# Stacks are LIFO (Last-In First-Out) structures. The last thing we put in them is the first thing we can remove or retrieve


# Implementation using a list
example = []
example.append('item 1')
example.append('item 2')
example.append('item 3')

example.pop()
# example list now only has items 1 and 2 in it
print(example)

# lists in Python are dynamic arrays. This means they can be computationally costly when you need to expand the size of your structure.

# this is why it is preferable to use a deque, imported from the 'collections library'
# from collections import deque

# stack = deque()

