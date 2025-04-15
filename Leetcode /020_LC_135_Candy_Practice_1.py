#https://leetcode.com/problems/candy/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        n = len(ratings)
        # Step 2: Left to right scan
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left scan
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
        
        