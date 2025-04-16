#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        char_index = {}
        start = 0
        max_len = 0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                # Found a repeat character → move start
                start = char_index[s[end]] + 1

            char_index[s[end]] = end  # Update last seen index
            max_len = max(max_len, end - start + 1)

        return max_len