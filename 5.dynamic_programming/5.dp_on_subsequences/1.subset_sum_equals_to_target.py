# Subset sum equals to target
"""
Given an array arr of n integers and an integer target,
determine if there is a subset of the given array with a sum equal to the given target.
"""
"""
Example 1:
Input: arr = [1, 2, 7, 3], target = 6
Output: True
Explanation: There is a subset (1, 2, 3) with sum 6.


Example 2:
Input: arr = [2, 3, 5], target = 6
Output: False
Explanation: There is no subset with sum 6.
"""
"""
Constraints
- 1 <= n = 100
- 1 <= n = 100
- 0<= target <= 5*103
"""


class Solution:
    def f(self, ind, arr, target):
        if ind == 0:
            return arr[0]

        if arr[ind] > target:
            return float("inf")

        for i in range(ind):
            kemp = arr[ind] + self.func(i, arr, target)

    def isSubsetSum(self, arr, target):
        self.count = 0
