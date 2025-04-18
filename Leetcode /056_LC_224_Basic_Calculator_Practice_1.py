#https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  # 1 means +, -1 means -

        result = 0
        i = 0
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                continue  # skip increment since we advanced in inner loop

            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                # Push current result and sign
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                # Complete sub-expression
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            # Ignore spaces

            i += 1

        return result
