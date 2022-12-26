class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""

head            current_node
 |              |
 |              |
 V              |
Node            V
  value: 8
  next: ------> Node
                  value: 24
                  next: -----------> Node
                                       value: -4
                                       next: None
"""


def from_start(head: Node, index: int) -> int:
    """
    :param head: the first node in the linked list
    :param index: the index from the start, zero-based
    :return: the value of the node at the given index
    """
    current_node = head
    
    for i in range(index+1):
        current_node = current_node.next
        
    return current_node.value
    # head.value # get the value
    # head.next # the next Node
    
    

        