"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Pass 1: Weave the list
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        # Pass 2: Set the random pointers
        curr = head
        while curr:
            if curr.random:
                # random pointer of the copy = randommppinter of its original
                curr.next.random = curr.random.next
            # hop 2 to visit only the copies
            curr = curr.next.next 
            
        # Pass 3: Separate the lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next  # Restore original and skip copy
            if copy.next: #original copy
                copy.next = copy.next.next # Link copies, woow now i see it.
            curr = curr.next
            
        return copy_head