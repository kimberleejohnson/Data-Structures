# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Start at the root, create a variable to store current node 
    current_node = self 
    # Create a boolean for your while loop 
    robot_light = True

    while robot_light: 
      # If the insert value is smaller than the current node value, and you can still move left, move to left 
      if value < current_node.value and current_node.left: 
        current_node = current_node.left 
      # Else if greater, and you can move right, move to right 
      elif value > current_node.value and current_node.right: 
        current_node = current_node.right 
      # Else if value is less than current node, but you've reached the end and can't move left 
      # That's where you need to insert the value 
      elif value < current_node.value and not current_node.left: 
        current_node.left = BinarySearchTree(value)
        robot_light = False 
      elif value > current_node.value and not current_node.right: 
        current_node.right = BinarySearchTree(value)
        robot_light = False 

  def contains(self, target):
    # Start at the root, create variable to store current node
    current_node = self 
    
    # Create a boolean for running your while loop 
    robot_light = True 
    
    while robot_light: 
      # If target is current node
      if target is current_node.value: 
        # You've found the value! Turn off your boolean
        robot_light = False 
        # Return True  
        return True 
      # Else if target less than current node, and can move left
      elif current_node.value >= target and current_node.left: 
        # Make left node your current 
        current_node = current_node.left
      # But what if you've searched the whole list? Can't go right any more.  
      elif current_node.value >= target and not current_node.left: 
        robot_light = False 
        return False 
      # Else if target greater than current node, and can move right 
      elif current_node.value <= target and current_node.right: 
        current_node = current_node.right
      # But what if you've gone through the whole list? 
      elif current_node.value <= target and not current_node.right: 
        robot_light = False 
        return False 
  

  def get_max(self):
    # Start at the root, create variable to hold current node and current highest value 
    current_node = self 
    current_highest = self.value 

    # Boolean for loop 
    robot_light = True 

    while robot_light: 
      # Keep moving to the right until you no longer can 
      if current_node.right: 
        current_node = current_node.right 
      # But, if you *can't* move to the right any more 
      elif not current_node.right: 
        # Stop the loop 
        robot_light = False 
      # And evaluate, resetting highest value if you need 
      if current_node.value >= current_highest: 
        current_highest = current_node.value
    return current_highest 

  def for_each(self, cb):
    # We want to perform a function on every item in the tree
    # Start with the current value, perform it  
    # If you can move right, call the newly defined function passing in cb
    # If you can move left, keep performing the callback 

    current_node = self 

    cb(current_node.value)

    if current_node.right: 
      current_node.right.for_each(cb)
    
    if current_node.left: 
      current_node.left.for_each(cb)