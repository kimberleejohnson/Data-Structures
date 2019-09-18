import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Start at the root 
    # If the element already there, return None because no duplicates 
    # If not there, then split the tree in half (left or right side), and determine which side value should go 
    # Repeat 
    pass

  def contains(self, target):
    # Start at the root 
    # Compare the target to the root. Based on comparison, go left (target lower) or right (target higher)
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass