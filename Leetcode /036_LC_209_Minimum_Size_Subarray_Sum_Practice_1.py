#209. Minimum Size Subarray Sum
#https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        min_length = float('inf')

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
