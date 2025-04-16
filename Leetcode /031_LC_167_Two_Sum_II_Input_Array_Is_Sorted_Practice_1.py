#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Add 1 to each index since the array is 1-indexed
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
