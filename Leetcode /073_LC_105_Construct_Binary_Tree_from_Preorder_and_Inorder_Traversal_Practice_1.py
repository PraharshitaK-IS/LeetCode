# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a map for quick index lookup in inorder traversal
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, in_start, in_end):
            if pre_start >= len(preorder) or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            in_index = inorder_index[root_val]
            left_tree_size = in_index - in_start
            
            root.left = helper(pre_start + 1, in_start, in_index - 1)
            root.right = helper(pre_start + 1 + left_tree_size, in_index + 1, in_end)
            
            return root
        
        return helper(0, 0, len(inorder) - 1)
