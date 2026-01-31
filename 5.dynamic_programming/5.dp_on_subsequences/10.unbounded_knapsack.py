# Unbounded knapsack
"""
Given two integer arrays, val and wt, each of size N, representing the values and weights of N items respectively,
and an integer W,
representing the maximum capacity of a knapsack,
determine the maximum value achievable by selecting a subset of the items such that the total
weight of the selected items does not exceed the knapsack capacity W.
The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.

An infinite supply of each item can be assumed.
"""
"""
Example 1:
Input: val = [5, 11, 13], wt = [2, 4, 6], W = 10
Output: 27
Explanation: Select 2 items with weights 4 and 1 item with weight 2 for a total value of 11+11+5 = 27.

Example 2:
Input: val = [10, 40, 50, 70], wt = [1, 3, 4, 5], W = 8
Output: 110
Explanation: Select items with weights 3 and 5 for a total value of 40 + 70 = 110.
"""
"""
Constraints:
- 1 ≤ N ≤ 500
- 1 ≤ W ≤ 1000
- 1 ≤ wt[i] ≤ 500
- 1 ≤ val[i] ≤ 500
"""


class Solution:
    def f(self, ind, target, arr, wt, dp):
        if ind < 0:
            return 0
        if target == 0:
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = 0
        if wt[ind] <= target:
            take = arr[ind] + self.f(ind, target - wt[ind], arr, wt, dp)
        not_take = 0 + self.f(ind - 1, target, arr, wt, dp)

        dp[ind][target] = max(take, not_take)

        return max(take, not_take)

    def unboundedKnapsack(self, wt, val, n, W):
        dp = [[-1] * (W + 1) for _ in range(n)]
        return self.f(n - 1, W, val, wt, dp)


class SolutionOptimal:
    def unboundedKnapsack(self, wt, val, n, W):
        dp = [[0] * (W + 1) for _ in range(n)]

        for i in range(W + 1):
            dp[0][i] = (i // wt[0]) * val[0]

        for ind in range(1, n):
            for tar in range(W + 1):
                take = 0
                if wt[ind] <= tar:
                    take = val[ind] + dp[ind][tar - wt[ind]]
                not_take = 0 + dp[ind - 1][tar]

                dp[ind][tar] = max(take, not_take)

        return dp[n - 1][W]


class SolutionOptimalSpace:
    def unboundedKnapsack(self, wt, val, n, W):
        # dp = [[0] * (W + 1) for _ in range(n)]
        prev, curr = [0] * (W + 1), [0] * (W + 1)

        for i in range(W + 1):
            prev[i] = (i // wt[0]) * val[0]

        for ind in range(1, n):
            curr = [0] * (W + 1)
            for tar in range(W + 1):
                take = 0
                if wt[ind] <= tar:
                    take = val[ind] + curr[tar - wt[ind]]
                not_take = 0 + prev[tar]

                curr[tar] = max(take, not_take)

            prev = curr

        return prev[W]


s = SolutionOptimalSpace()

k1 = s.unboundedKnapsack(
    [2, 4, 6],
    [5, 11, 13],
    3,
    10,
)

k2 = s.unboundedKnapsack(
    [1, 3, 4, 5],
    [10, 40, 50, 70],
    4,
    8,
)

print(k1)
print(k2)
