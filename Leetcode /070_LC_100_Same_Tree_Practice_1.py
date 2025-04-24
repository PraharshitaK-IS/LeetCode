#https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == None or q == None):
            if(p==q):
                return True
            else:
                return False
        if(self.isSameTree(p.left,q.left) and  self.isSameTree(p.right,q.right) and p.val == q.val):
            return True
        else:
            return False
        
        