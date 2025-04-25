#Found this tough, come back to it.
#https://leetcode.com/problems/number-of-islands/


from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            # Base case: if we're out of bounds or at water, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the land as visited by changing it to '0'
            grid[r][c] = '0'
            
            # Explore all 4 directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)  # Start DFS to mark the whole island
        
        return island_count
