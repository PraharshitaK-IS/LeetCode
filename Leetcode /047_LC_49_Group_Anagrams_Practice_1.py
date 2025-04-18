#https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word and use the sorted version as a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        # Return all the grouped anagram lists
        return list(anagram_map.values())
