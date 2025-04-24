#THIS ONE WAS TOUGH - COME BACK TO IT LATER AND TRACE
#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # Start with the root of the tree
        curr = root

        while curr:
            # Dummy node that builds the next level
            dummy = Node(0)
            tail = dummy

            # Iterate over the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # Move to next node in current level

            # Move to the first node of the next level
            curr = dummy.next

        return root
