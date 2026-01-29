# 0 1 Knapsack problem
"""
Given two integer arrays, val and wt, each of size N, which represent the values and weights of N items respectively,
and an integer W representing the maximum capacity of a knapsack,
determine the maximum value achievable by selecting a subset of the items such that the total weight
of the selected items does not exceed the knapsack capacity W.

Each item can either be picked in its entirety or not picked at all (0-1 property).
The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.
"""
"""
Example 1:
Input: val = [60, 100, 120], wt = [10, 20, 30], W = 50
Output: 220
Explanation: Select items with weights 20 and 30 for a total value of 100 + 120 = 220.


Example 2:
Input: val = [10, 40, 30, 50], wt = [5, 4, 6, 3], W = 10
Output: 90
Explanation: Select items with weights 4 and 3 for a total value of 40 + 50 = 90.
"""
"""
Constraints
- 1 ≤ N ≤ 500
- 1 ≤ W ≤ 1000
- 1 ≤ wt[i] ≤ 500
- 1 ≤ val[i] ≤ 500
"""


class Solution:
    def f(self, ind, target, arr, wt, dp):
        if ind == 0:
            return arr[0] if wt[0] <= target else 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = float("-inf")
        if wt[ind] <= target:
            take = arr[ind] + self.f(ind - 1, target - wt[ind], arr, wt, dp)
        not_take = 0 + self.f(ind - 1, target, arr, wt, dp)

        dp[ind][target] = max(take, not_take)

        return max(take, not_take)

    def knapsack01(self, wt, val, n, W):
        dp = [[-1] * (W + 1) for _ in range(n)]
        return self.f(n - 1, W, val, wt, dp)


class SolutionOptimal:
    def knapsack01(self, wt, val, n, W):
        dp = [[0] * (W + 1) for _ in range(n)]

        for i in range(wt[0], W):
            dp[0][i] = val[0]

        for ind in range(1, n):
            for tar in range(1, W + 1):
                take = float("-inf")
                if wt[ind] <= tar:
                    take = val[ind] + dp[ind - 1][tar - wt[ind]]
                not_take = 0 + dp[ind - 1][tar]

                dp[ind][tar] = max(take, not_take)

        return dp[n - 1][W]


class SolutionOptimalSpace2D:
    def knapsack01(self, wt, val, n, W):
        if n < 2:
            return val[0] if wt[0] <= W else 0

        prev, curr = [0] * (W + 1), [0] * (W + 1)

        for i in range(wt[0], W):
            prev[i] = val[0]

        for ind in range(1, n):
            curr = [0] * (W + 1)
            for tar in range(W + 1):
                take = float("-inf")
                if wt[ind] <= tar:
                    take = val[ind] + prev[tar - wt[ind]]
                not_take = 0 + prev[tar]

                curr[tar] = max(take, not_take)

            prev = curr

        return prev[W]


class SolutionOptimalSpace1D:
    def knapsack01(self, wt, val, n, W):
        if n < 2:
            return val[0] if wt[0] <= W else 0

        prev = [0] * (W + 1)

        for i in range(wt[0], W):
            prev[i] = val[0]

        for ind in range(1, n):
            for tar in range(W, -1, -1):
                take = float("-inf")
                if wt[ind] <= tar:
                    take = val[ind] + prev[tar - wt[ind]]
                not_take = 0 + prev[tar]

                prev[tar] = max(take, not_take)

        return prev[W]


s = SolutionOptimalSpace1D()

k1 = s.knapsack01([10, 20, 30], [60, 100, 120], 3, 50)

k2 = s.knapsack01([5, 4, 6, 3], [10, 40, 30, 50], 4, 10)

print(k1)
print(k2)
