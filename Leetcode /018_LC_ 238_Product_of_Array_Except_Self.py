#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        
        # Prefix product
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Postfix product
        postfix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
