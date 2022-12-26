class Node:
    def __init__(self, value):
        self.value = value
        self.prev= None
        self.next = None
        
        
class LinkedList:
    #write your code here
    def __init__(self):
        self.head = None
        self.tail= None
        
        def add_first(self, value):
            new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, value):
        #write your code here
        new_node = Node(value)
        
        if (self.head == None):
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
            return
        else:
            
            self.tail.next = new_node
            new_node.prev= self.tail
            self.tail = new_node
            self.tail.next = None

        