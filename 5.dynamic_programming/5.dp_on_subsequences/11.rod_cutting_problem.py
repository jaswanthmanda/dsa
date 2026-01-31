# Rod cutting problem
"""
Given a rod of length N inches and an array price[] where price[i] denotes the value
of a piece of rod of length i inches (1-based indexing).
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
Make any number of cuts, or none at all, and sell the resulting pieces.
"""
"""
Example 1:
Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
Output: 25
Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.

Example 2:
Input: price = [1, 5, 8, 9], N = 4
Output: 10
Explanation: Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.
"""
"""
Constraints
- 1 ≤ N ≤ 1000
- 1 ≤ price[i] ≤ 10^5
"""


class Solution:
    def f(self, ind, target, arr, dp):
        if target == 0:
            return 0
        if ind < 0:
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = 0
        if (ind + 1) <= target:
            take = arr[ind] + self.f(ind, target - (ind + 1), arr, dp)
        not_take = 0 + self.f(ind - 1, target, arr, dp)

        dp[ind][target] = max(take, not_take)

        return max(take, not_take)

    def RodCutting(self, price, n):
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.f(n - 1, n, price, dp)


class SolutionOptimal:
    def RodCutting(self, price, n):
        dp = [[0] * (n + 1) for _ in range(n)]

        for i in range(n + 1):
            dp[0][i] = i * price[0]

        for ind in range(1, n):
            for tar in range(1, n + 1):
                take = 0
                if (ind + 1) <= tar:
                    take = price[ind] + dp[ind][tar - (ind + 1)]
                not_take = 0 + dp[ind - 1][tar]

                dp[ind][tar] = max(take, not_take)

        return dp[n - 1][n]


class SolutionOptimalSpace:
    def RodCutting(self, price, n):
        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for i in range(n + 1):
            prev[i] = i * price[0]

        for ind in range(1, n):
            curr = [0] * (n + 1)
            for tar in range(1, n + 1):
                take = 0
                if (ind + 1) <= tar:
                    take = price[ind] + curr[tar - (ind + 1)]
                not_take = 0 + prev[tar]

                curr[tar] = max(take, not_take)

            prev = curr

        return prev[n]


s = SolutionOptimalSpace()

k1 = s.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8)

k2 = s.RodCutting([1, 5, 8, 9], 4)

k3 = s.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8)

print(k1)
print(k2)
print(k3)
