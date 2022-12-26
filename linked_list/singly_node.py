class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
# Defines a node in a singly linked list


# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    # Method. Adds a new node with the specific data value to the beginning of the linked list.
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Method. Returns the value in the first node in the linked list.
    # Returns None if the list is empty.
    def get_first(self):
        pass

    # Method. Returns the value of the last node in the linked list. Returns None if the list is empty.
    def get_first(self):
        #write your code here
        if self.head is None:
            return None
        return self.head.val

    # Method. Returns the value at a given index in the linked list.
    # Index count starts at 0.
    # Returns None if there are fewer nodes in the linked list than the index value.
    def get_at_index(self, index):
        pass       
    
    def search(self, value):
        current = self.head

        while current:
            if current.val == value:
                return True
            current = current.next
        
        return False
    
    
    def get_at_index(self, index):
        #write your code here
        current = self.head
        count = 0
        # loop till current not equal to None
        while current != None:
            if count == index:
                return current.val 
            count +=1
            current = current.next

        return None 
    
    
    def add_last(self, value):
        #write your code here
        new_node = Node(value)
        
        if (self.head == None):
            self.head = new_node
            return
        else:
            current = self.head
            
            while current.next != None:
                current = current.next
            
            current.next = new_node
            
            
            
    def remove(self, index):
        if not self.head:
            return 

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        current_index = 0
        while current.next and current_index < index - 1:
            current = current.next
            current_index += 1

        if current.next:
            current.next = current.next.next