# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap to store value -> its index in inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1  # Start from the end of postorder
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            # Pick up the current root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(root_val)
            
            # Build right subtree first (because postorder is L → R → Root)
            index = inorder_index[root_val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
