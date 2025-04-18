#https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
       
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue  # Skip empty and current directory
            elif part == '..':
                if stack:
                    stack.pop()  # Go up one level
            else:
                stack.append(part)  # Valid directory name

        return '/' + '/'.join(stack)
