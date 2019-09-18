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
      # Else if target less than current node
      elif target < current_node.value: 
        # Make left node your current 
        current_node.value = current_node.left 
      # Otherwise, your target must be greater than 
      else:  
        # Make right node your current
        current_node.value = current_node.right 
  

  def get_max(self):
    pass

  def for_each(self, cb):
    pass