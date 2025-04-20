#Objective: To find out if the distance between two same numbers in the array is less than or equal to K.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int):
        index_map = {}  # Stores num -> last seen index

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update to latest index
        return False