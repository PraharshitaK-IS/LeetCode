#https://leetcode.com/problems/two-sum/

#Objective: Find the index of two complementary numbers
#Solution: Use a map to track the number and its index. Everytime we go to a new number, check for its complement before adding it.

def twoSum(nums, target):
    num_map = {}  # Dictionary to store value: index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i