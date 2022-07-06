# Predict the Following Output
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


b = Node(5)
c = Node(True)
d = Node("hello world")
e = Node(7)
f = Node(10) 

b.next = c
c.next = d
d.next = e
e.next = f

print(b.next.value)
print(b.next.next.next.value)
