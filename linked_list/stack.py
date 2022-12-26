class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, item):
        self.store.add_first(item)

    def pop(self):
        return self.store.remove_first()

    def empty(self):
        return self.store.length() == 0