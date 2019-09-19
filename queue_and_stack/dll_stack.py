import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    self.storage = DoublyLinkedList(); 

  # Push is adding an item to the top of the stack (FILO)
  def push(self, value):
    self.size += 1
    self.storage.add_to_head(value)
  
  # Pop is removing an item from the top of the list (FILO)
  def pop(self):
    # As long as the stack is not length of 0
    if self.size > 0:
      # Decrement the length of the queue
      self.size -= 1
      head_item = self.storage.head
      self.storage.remove_from_head()
      return head_item.value 
    else: 
      return None 

  def len(self):
    return self.storage.__len__()
