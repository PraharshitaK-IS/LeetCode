#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip(' ').split(' ')
        return len(words[-1])