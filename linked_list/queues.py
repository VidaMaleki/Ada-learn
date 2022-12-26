# first in first out (FIFO)

class Queue:
    def __init__(self):
        self.store = LinkedList.new

    def enqueue(self, item):
        self.store.add_last(item)

    def dequeue(self):
        if self.is_empty():
            return None

        self.store.remove_first()

    def is_empty(self):
        return self.store.empty()