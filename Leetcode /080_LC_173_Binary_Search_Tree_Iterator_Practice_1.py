#https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack for the simulation of the in-order traversal
        self.stack = []
        # Push the leftmost path from the root onto the stack
        self._push_left_branch(root)

    def _push_left_branch(self, node: Optional[TreeNode]):
        # Helper function to go as left as possible
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest number
        node = self.stack.pop()
        val = node.val
        # If the node has a right child, push its left branch
        if node.right:
            self._push_left_branch(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()