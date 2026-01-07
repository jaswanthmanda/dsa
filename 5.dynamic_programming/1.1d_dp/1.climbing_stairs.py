# Climbing stairs
"""
Given an integer n, there is a staircase with n steps, starting from the 0th step.

Determine the number of unique ways to reach the nth step, given that each move can be either 1 or 2 steps at a time.
"""
"""
Example 1:
Input: n = 2
Output: 2
Explanation:
There are 2 unique ways to climb to the 2nd step:
1) 1 step + 1 step
2) 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation:
There are 3 unique ways to climb to the 3rd step:
1) 1 step + 1 step + 1 step
2) 2 steps + 1 step
3) 2 steps + 1 step
"""
"""
Constraints:
- 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n):
        if n <= 1:
            return n

        prev2 = 0
        prev = 1
        curr = 0
        for i in range(2, n + 2):
            curr = prev2 + prev
            prev2 = prev
            prev = curr

        return curr


s = Solution()

k1 = s.climbStairs(5)

print(k1)
