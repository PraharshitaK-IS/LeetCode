#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map:
                # Pop from stack if non-empty, else use dummy '#'
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)

        return not stack  # Valid if stack is empty
