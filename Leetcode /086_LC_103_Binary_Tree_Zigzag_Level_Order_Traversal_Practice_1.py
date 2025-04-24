#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        left_to_right = True          # flip after every level
        result = []

        while q:
            level_size = len(q)
            level = deque()           # lets us O(1) insert on either side

            for _ in range(level_size):
                node = q.popleft()

                # Append on the left or right depending on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                # normal BFS expansion
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right   # flip direction

        return result
