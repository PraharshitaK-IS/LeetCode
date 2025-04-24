#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Connect the right subtree to the rightmost node
                rightmost.right = curr.right
                
                # Move left subtree to the right
                curr.right = curr.left
                curr.left = None  # Set left to None as required
            
            # Move to the next node (right child)
            curr = curr.right
