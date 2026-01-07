import sys

# Frog jump with k distances
"""
A frog wants to climb a staircase with n steps. Given an integer array heights,
where heights[i] contains the height of the ith step, and an integer k.

To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy,
where abs() denotes the absolute difference.
The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists.

Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
"""
"""
Example 1
Input: heights = [10, 5, 20, 0, 15], k = 2
Output: 15
Explanation:
0th step -> 2nd step, cost = abs(10 - 20) = 10
2nd step -> 4th step, cost = abs(20 - 15) = 5
Total cost = 10 + 5 = 15.

Example 2:
Input: heights = [15, 4, 1, 14, 15], k = 3
Output: 2
Explanation:
0th step -> 3rd step, cost = abs(15 - 14) = 1
3rd step -> 4th step, cost = abs(14 - 15) = 1
Total cost = 1 + 1 = 2.
"""
"""
Constraints
- 1 <= n <= 104
- 1 <= k <= 10
- 0 <= heights[i] <= 104
"""


class Solution:
    def f(self, k, ind, heights, dp):
        if ind == 0:
            return 0

        if dp[ind] != -1:
            return dp[ind]

        item = sys.maxsize

        for i in range(ind - 1, max(-1, ind - k - 1), -1):
            item = min(
                item,
                self.f(k, i, heights, dp) + abs(heights[ind] - heights[i]),
            )

        dp[ind] = item

        return dp[ind]

    def frogJump(self, heights, k):
        n = len(heights)

        dp = [-1] * (n + 1)

        return self.f(k, n - 1, heights, dp)


s = Solution()

k1 = s.frogJump([10, 5, 20, 0, 15], 2)

k2 = s.frogJump([15, 4, 1, 14, 15], 3)

print(k1)
print(k2)
