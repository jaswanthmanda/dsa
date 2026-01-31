# Coin Change II
"""
Give an array coins of n integers representing coin denominations.
 Your task is to find the number
of distinct combinations that sum up to a specified amount of money.
If it's impossible to achieve the exact amount with any combination of coins, return 0.

Single coin can be used any number of times.

Return your answer with modulo 109+7.
"""
"""
Example 1:
Input: coins = [2, 4,10], amount = 10
Output: 4
Explanation: The four combinations are:
10 = 10
10 = 4 + 4 + 2
10 = 4 + 2 + 2 + 2
10 = 2 + 2 + 2 + 2 + 2

Example 2:
Input: coins = [5], amount = 5
Output: 1
Explanation: There is one combination: 5 = 5.
"""
"""
Constraints
- 1 <= n, coins[i], amount <= 103
- All the values of coins are unique.
"""


class Solution:
    def f(self, ind, target, arr, dp):
        if target == 0:
            return 1

        if ind < 0:
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = 0
        if arr[ind] <= target:
            take = self.f(ind, target - arr[ind], arr, dp)
        notTake = self.f(ind - 1, target, arr, dp)

        dp[ind][target] = take + notTake

        return take + notTake

    def count(self, coins, N, amount):
        dp = [[-1] * (amount + 1) for _ in range(N)]
        return self.f(N - 1, amount, coins, dp)


class SolutionOptimal:
    def count(self, coins, N, amount):
        MOD = (10**9) + 7
        dp = [[0] * (amount + 1) for _ in range(N)]

        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for ind in range(1, N):
            for tar in range(amount + 1):
                take = 0
                if coins[ind] <= tar:
                    take = dp[ind][tar - coins[ind]]
                notTake = dp[ind - 1][tar]

                dp[ind][tar] = take + notTake

        return dp[N - 1][amount] % MOD


class SolutionOptimalSpace:
    def count(self, coins, N, amount):
        MOD = (10**9) + 7
        prev, curr = [0] * (amount + 1), [0] * (amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1

        for ind in range(1, N):
            curr = [0] * (amount + 1)
            for tar in range(amount + 1):
                take = 0
                if coins[ind] <= tar:
                    take = curr[tar - coins[ind]]
                notTake = prev[tar]

                curr[tar] = take + notTake

            prev = curr

        return prev[amount] % MOD


s = SolutionOptimalSpace()

k1 = s.count(
    [2, 4, 10],
    3,
    10,
)

k2 = s.count(
    [5],
    1,
    5,
)

print(k1)
print(k2)
