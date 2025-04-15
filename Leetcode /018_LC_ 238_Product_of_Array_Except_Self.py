#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        for i in range(0,length):
            for j in range(0,length):
                if(i==j):
                    continue
                answer[i] = answer[i] * nums[j]
        
        return answer