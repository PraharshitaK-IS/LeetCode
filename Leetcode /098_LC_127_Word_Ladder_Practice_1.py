#https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, depth = queue.popleft()
            if current_word == endWord:
                return depth

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != current_word[i]:
                        mutated = current_word[:i] + c + current_word[i+1:]
                        if mutated in word_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, depth + 1))
        
        return 0