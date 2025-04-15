#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    # Pointer to place next allowable element
    k = 2

    for i in range(2, len(nums)):
        # Compare current element with element at k-2
        # If not equal, we can safely place it
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k