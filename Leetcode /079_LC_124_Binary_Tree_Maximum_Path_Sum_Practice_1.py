#https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # global maximum path sum

        def dfs(node):
            if not node:
                return 0

            # Recursively get the max gain from left and right, ignore negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Max path sum **with split at current node**
            current_sum = node.val + left + right
            self.max_sum = max(self.max_sum, current_sum)

            # For parent, return max gain of extending the path
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum