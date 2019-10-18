class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # if the current is up to  the capacity
        if self.current == self.capacity:
            # set the current to 0 again
            self.current = 0
        # insert into the storage at position current
        self.storage[self.current] = item
        # increment current
        self.current += 1

    def get(self):
        # return the element in the storage
        # do not return None, use list comprehension
        return [item for item in self.storage if item is not None]
