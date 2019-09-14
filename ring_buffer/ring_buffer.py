class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if None in self.storage:
      first_index = self.storage.index(None)
      self.storage[first_index] = item
    else:
      self.storage[self.current] = item
      if self.current < self.capacity -1:
        self.current += 1
    
  def get(self):
    output = [item for item in self.storage if item != None]

    return output
    

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

buffer.append('d')

print(buffer.get())