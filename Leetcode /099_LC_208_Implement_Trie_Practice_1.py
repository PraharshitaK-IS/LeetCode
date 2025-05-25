#https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    __slots__ = ("children", "isEnd")

    def __init__(self):
        self.children = [None] * 26   # 26 letters a–z
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # ---------------- public API ----------------
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - 97               # ord('a') == 97
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    # ---------------- internal helper ----------------
    def _traverse(self, s: str) -> TrieNode | None:
        """Return the node reached after consuming s, or None if the path breaks."""
        node = self.root
        for ch in s:
            idx = ord(ch) - 97
            node = node.children[idx]
            if node is None:
                return None
        return node
