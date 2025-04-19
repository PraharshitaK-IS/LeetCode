#https://leetcode.com/problems/copy-list-with-random-pointer/

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

        # Dictionary to hold old nodes as keys and new nodes as values
        old_to_new = {}

        # First pass: Copy all the nodes and put them in the hashmap
        current = head
        while current:
            copy = Node(current.val)
            old_to_new[current] = copy
            current = current.next

        # Second pass: Assign next and random pointers
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]