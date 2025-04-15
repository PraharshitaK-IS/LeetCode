
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer to the position of the last unique element
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k