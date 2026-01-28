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
    def f(self, ind, target, arr, dp):
        if target == 0:
            return True
        if ind < 0:
            return False

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = False

        if arr[ind] <= target:
            take = self.f(ind - 1, target - arr[ind], arr, dp)
        not_take = self.f(ind - 1, target, arr, dp)

        dp[ind][target] = take or not_take

        return take or not_take

    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[-1] * (target + 1) for _ in range(n)]
        return self.f(len(arr) - 1, target, arr, dp)


class SolutionOptimal:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        dp = [[False] * (target + 1) for _ in range(n)]

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(n):
            dp[i][0] = True

        for ind in range(1, n):
            for j in range(1, target + 1):
                take = False
                if arr[ind] <= j:
                    take = dp[ind - 1][j - arr[ind]]
                not_take = dp[ind - 1][j]

                dp[ind][j] = take or not_take

        return dp[n - 1][target]


class SolutionOptimalSpace:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        curr, prev = [False] * (target + 1), [False] * (target + 1)

        prev[0] = True

        if arr[0] <= target:
            prev[arr[0]] = True
        for ind in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for j in range(1, target + 1):
                take = False
                if arr[ind] <= j:
                    take = prev[j - arr[ind]]
                not_take = prev[j]

                curr[j] = take or not_take
            prev = curr

        return prev[target]


s = SolutionOptimalSpace()

k1 = s.isSubsetSum(
    [
        1,
        2,
        7,
        3,
    ],
    6,
)

k2 = s.isSubsetSum(
    [
        2,
        3,
        5,
    ],
    6,
)

print(k1)
print(k2)
