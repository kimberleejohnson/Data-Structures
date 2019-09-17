import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# What is an LRU Cache? 
## A data structure built on top of DLL that stores key:value pairs in list nodes. 
## Head is considered the oldest; tail is considered newest, e.g. most recently used. 

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    # Max number of nodes 
    self.limit = limit 
    # Current number of nodes 
    self.nodes = 0 
    # DoublyLinkedList holding entries in correct order 
    self.cache = DoublyLinkedList() 
    # Storage dict for every node in cache
    self.storage = {} 

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):

    # Return None if the key-value pair doesn't exist in the cache. 
    if self.nodes is 0 or key not in self.storage: 
      return None 

    #Otherwise, 
    else: 
      # Sets value 
      value = self.storage[key]
      # Remove old node
      self.cache.delete(value[1])
      # Assign node to front of DLL cache 
      self.cache.add_to_head([key, value[0]])
      # Return the value associated with the key 
      return value[0]
    

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # If the key is in the dictionary to begin with 
    if key in self.storage: 
      # Value in storage 
      storage_value = self.storage[key]
      # Delete the old storage value 
      self.cache.delete(storage_value[1])
      # New value added to the front 
      self.cache.add_to_head([key, value])
      self.storage[key] = [value, self.cache.head]
      return 
    
    # If the cache already at capacity, remove the oldest entry to make room 
    if self.limit is self.nodes: 
      old_node = self.cache.tail 
      self.cache.remove_from_tail()
      del self.storage[old_node.value[0]]
      self.nodes -= 1
    
    self.cache.add_to_head([key, value])
    self.storage[key] = [value, self.cache.head]
    self.nodes += 1 
