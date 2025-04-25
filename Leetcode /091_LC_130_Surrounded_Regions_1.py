#Found tough, return and trace
#https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
                return
            
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Base case: if out of bounds or not 'O', stop
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the cell as safe
            board[r][c] = 'S'
            
            # Recurse in all 4 directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # 1. Start DFS from all border 'O's
        for r in range(rows):
            dfs(r, 0)       # left border
            dfs(r, cols - 1)  # right border
        for c in range(cols):
            dfs(0, c)       # top border
            dfs(rows - 1, c)  # bottom border
        
        # 2. Flip the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # surrounded
                elif board[r][c] == 'S':
                    board[r][c] = 'O'  # safe
