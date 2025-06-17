#https://leetcode.com/problems/word-search-ii/

from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates
                # aggressively prune if this was the only path
                if not next_node.children:
                    node.children.pop(ch)
                    return

            board[i][j] = '#'
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, next_node)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, root)

        return result
