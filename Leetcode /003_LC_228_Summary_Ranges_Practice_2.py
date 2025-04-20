#https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            # If current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start = nums[i]  # Start new range

        # Append the final range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges
