import sys

# Frog jump
"""
A frog wants to climb a staircase with n steps.
Given an integer array heights, where heights[i] contains the height of the ith step.

To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy,
where abs() denotes the absolute difference. The frog can jump from any step either one or two steps, provided it exists.

Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
"""
"""
Example 1
Input: heights = [2, 1, 3, 5, 4]
Output: 2
Explanation:
One possible route can be,
0th step -> 2nd Step = abs(2 - 3) = 1
2nd step -> 4th step = abs(3 - 4) = 1
Total = 1 + 1 = 2.

Example 2:
Input: heights = [7, 5, 1, 2, 6]
Output: 9
Explanation:
One possible route can be,
0th step -> 1st Step = abs(7 - 5) = 2
1st step -> 3rd step = abs(5 - 2) = 3
3rd step -> 4th step = abs(2 - 6) = 4
Total = 2 + 3 + 4 = 9.
"""
"""
Constraints:
- 1 <= n <= 104
- 0 <= heights[i] <= 104
"""


class Solution:
    def f(self, ind, heights, dp):
        if ind == 0:
            return 0

        if dp[ind] != -1:
            return dp[ind]

        left = self.f(ind - 1 , heights, dp) + abs(heights[ind] - heights[ind - 1])

        right = sys.maxsize

        if ind > 1:
            right = self.f(ind - 2, heights, dp) + abs(heights[ind] - heights[ind - 2])

        dp[ind] = min(left, right)

        return dp[ind]

    def frogJump(self, heights):
        n = len(heights)

        dp = [-1] * (n + 1)

        return self.f(n - 1, heights, dp)


s = Solution()

k1 = s.frogJump([2, 1, 3, 5, 4])

k2 = s.frogJump([7, 5, 1, 2, 6])

print(k1)
print(k2)
