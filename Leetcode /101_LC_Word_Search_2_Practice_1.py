#https://leetcode.com/problems/word-search-ii/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Step 1: Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # Store full word at the leaf

        # Step 2: DFS function
        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            board[i][j] = "#"  # Mark visited
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != "#":
                    dfs(ni, nj, next_node)
            board[i][j] = ch  # Restore letter

        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return result
