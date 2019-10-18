class RingBuffer:
    """Implementation of the Ring Buffer data structure
    """

    def __init__(self, capacity):
        """Ring buffer constructor. Takes the fixed size of the ring buffer as capacity

        Arguments:
            capacity {int} -- Fixed size of the buffer
        """
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        """Adds an object to the buffer

        Arguments:
            item {object} -- object to be added to the buffer
        """
        # if the current is up to  the capacity
        if self.current == self.capacity:
            # set the current to 0 again
            self.current = 0

        # insert into the storage at position current
        self.storage[self.current] = item
        # increment current
        self.current += 1

    def get(self):
        """Returns the object in the ring buffer. Does not return None

        Returns:
            list -- the Ring Buffer storage
        """
        # return the element in the storage
        # do not return None, use list comprehension
        return [item for item in self.storage if item is not None]
