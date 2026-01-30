# Target sum
"""
Given an array nums of n integers and an integer target,
build an expression using the integers from nums where each integer
can be prefixed with either a '+' or '-' sign.

The goal is to achieve the target sum by evaluating all possible combinations of these signs.

Determine the number of ways to achieve the target sum and return your answer with modulo 10^9+7.
"""
"""
Example 1:
Input: nums = [1, 2, 7, 1, 5], target = 4
Output: 2
Explanation: There are 2 ways to assign symbols to make the sum of nums be target 4.
+1 + 2 + 7 - 1 - 5 = 4
-1 + 2 + 7 + 1 - 5 = 4


Example 2:
Input: nums = [1], target = 1
Output: 1
Explanation: There is only one way to assign symbols to make the sum of nums be target 1.
"""
"""
Constraints:
- 1 ≤ n ≤ 100
- 0 ≤ nums[i] ≤ 1000
- 0 <= sum(A[i]) <= 104
- -1000 <= target <= 1000
"""


class Solution:
    def targetSum(self, n, target, nums):
        ...
