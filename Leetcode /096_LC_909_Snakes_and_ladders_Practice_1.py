#https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
    
        def get_coordinates(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else (n - 1 - rem)
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (current_square, steps)

        while queue:
            s, steps = queue.popleft()
            for move in range(1, 7):  # dice roll
                next_s = s + move
                if next_s > n * n:
                    continue
                r, c = get_coordinates(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s == n * n:
                    return steps + 1
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, steps + 1))
        return -1