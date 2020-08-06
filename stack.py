from collections import deque

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

# Important to note that while I'm using this structure as a stack, "deque" in Python is a double-ended queue, which is a different structure entirely


# -----------------------------------------------------#
# COMMON CHALLENGES
#------------------------------------------------------#

# Reverse a stack:
# reverse_string("This stack is being reversed") should return "desrever gnieb si kcats sihT"

def reverse_string(argument):
    print(argument)
    stack = deque()
    output_holder = ""

    # Get all of the characters into the stack
    for char in argument:
      stack.append(char)

    stack_height = len(stack)
    idx = 0

    while (idx < stack_height):
      output_holder += (stack.pop())
      idx += 1
    

    print(output_holder)
