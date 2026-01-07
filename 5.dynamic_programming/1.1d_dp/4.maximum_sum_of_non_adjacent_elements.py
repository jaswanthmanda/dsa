# Maximum sum of non adjacent elements
"""
Given an integer array nums of size n.
Return the maximum sum possible using the elements of nums such
that no two elements taken are adjacent in nums.
"""
"""
Example 1:
Input: nums = [1, 2, 4]
Output: 5
Explanation:
[1, 2, 4], the underlined elements are taken to get the maximum sum.

Example 2:
Input: nums = [2, 1, 4, 9]
Output: 11
Explanation:
[2, 1, 4, 9], the underlined elements are taken to get the maximum sum.
"""
"""
Constraints
- n == nums.length
- 1 <= n <= 105
- 0 <= nums[i] <= 1000
"""


class Solution:
    def f(self, ind, nums, dp):
        if ind < 0:
            return 0
        elif ind == 0:
            return nums[0]

        if dp[ind] != -1:
            return dp[ind]

        take = nums[ind] + self.f(ind - 2, nums, dp)
        skip = self.f(ind - 1, nums, dp)

        dp[ind] = max(take, skip)

        return dp[ind]

    def nonAdjacent(self, nums):
        n = len(nums)

        dp = [-1] * (n + 1)

        return self.f(n - 1, nums, dp)


class SolutionOptimal:
    def func(self, n, nums):
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = 0
        prev = 0

        for x in nums:
            curr = max(prev, prev2 + x)
            prev2 = prev
            prev = curr

        return prev

    def nonAdjacent(self, nums):
        n = len(nums)

        return self.func(n, nums)


s = SolutionOptimal()

k1 = s.nonAdjacent([1, 2, 4])

k2 = s.nonAdjacent([2, 1, 4, 9])

print(k1)
print(k2)
