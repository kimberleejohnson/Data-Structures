import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # DLL to store our elements in a queue because we constantly change the length of
    self.storage = DoublyLinkedList() 
    

  # Insertion is "enqueue" 
  # To add an item in a queue, we need to add that item to the front of the end of the list (FILO)
  def enqueue(self, value):
    # Increase length of list by 1
    self.size += 1
    # Add new item to back of list
    self.storage.add_to_tail(value)
  
  # Deletion is "dequeue"
  # To dequeue an item, we'll want to remove the item from the front of the last (FILO)
  def dequeue(self):
    # As long as the queue is not length of 0
    if self.size > 0:
      # Decrement the length of the queue
      self.size -= 1
      return self.storage.remove_from_head()
    else: 
      return None 

  # Returns the length of the queue
  def len(self):
    return self.storage.length
