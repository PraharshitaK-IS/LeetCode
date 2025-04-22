#https://leetcode.com/problems/jump-game-ii/

def jump(self, nums: List[int]) -> int:       
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):  # we don't need to jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            
    return jumps