# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Inserts a new element at the given position
  def push_at(self, newElement, position):     
    newNode = Node(newElement) 
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1):
      newNode.next = self.head
      self.head = newNode
    else:    
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None):
        newNode.next = temp.next
        temp.next = newNode  
      else:
        print("\nThe previous node is null.")

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code                 
MyList = LinkedList()

#Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

#Insert an element at position 2
MyList.push_at(100, 2)
MyList.PrintList() 

#Insert an element at position 1
MyList.push_at(200, 1)
MyList.PrintList()  

# The list contains: 10 20 30
# The list contains: 10 100 20 30
# The list contains: 200 10 100 20 30 