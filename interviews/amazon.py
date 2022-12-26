# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def middleNode(self, head):
#     end = head
#     count = 1
#     half = 1
    
#     while end.next != None: 
#         count += 1
#         end = end.next
    
#     if count % 2 == 0:
#         half = count // 2
#     else: 
#         half = count // 2
        
#     returnN = head
#     for i in range(1,half+1): 
#         returnN = returnN.next
    
#     return returnN




# add_to_back(self,val):
#     new_node = Node(val)
#     if self.head == None:
#         self.head=new_node
#     else:
#         runner = self.head
#         while runner != None:
#             Runner = runner.next
#         runner.next = new_node


# back(self, val):
#     if self.head == None:
#         return self.head
#     else:
#         runner = self.head
#         while runner != None:
#             runner = runner.next
#         return runner

# insert_ordered(self, new_value):
#     new_node = Node(new_value)
#     runner = self.head
#     while not (runner.value < new_value < runner.next.value):
#         runner = runner.next 
#     new_node.next = runner.next
#     runner.next = new_node


# middle(self, new_val):
#     # find the length first
#     if self.head == None:
#         return 0
# else:
#     counter = 0
#     runner = self.head
#     while runner != None:
#         counter += 1
#         runner = runner.next
#     # find the middle index
#     middle_index = counter // 2
#     #find the value of the middle element
#     new_runner = self.head
#     new_counter = 0
#     while new_counter < middle_index - 1
#         new_counter += 1
#         new_runner = new_runner.next
#     return new_runner.value
    
        
    
    
        
    
            

    


