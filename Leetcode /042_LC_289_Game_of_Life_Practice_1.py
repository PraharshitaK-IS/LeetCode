#https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        
        def countLiveNeighbors(r, c):
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == 1 or board[nr][nc] == -1:
                        live_neighbors += 1
            return live_neighbors

        # Step 1: Encode transitions in-place
        for r in range(m):
            for c in range(n):
                live_neighbors = countLiveNeighbors(r, c)

                # Rule 1 or 3: live cell dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1

                # Rule 4: dead cell becomes live
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        # Step 2: Decode final state
        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

            