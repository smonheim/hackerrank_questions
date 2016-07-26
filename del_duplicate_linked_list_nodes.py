"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
  orig = head
  while head.next:
    if head.next.data == head.data:
        if head.next.next:
            head.next = head.next.next
        else:
            head.next = None
    if head.next:
        if not(head.next.data == head.data):
            head = head.next
  return orig
