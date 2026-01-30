# Minimum coins
"""
Given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that are needed to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
There are infinite numbers of coins of each type
"""
"""
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.

Example 2:
Input: coins = [2, 5], amount = 3
Output: -1
Explanation: It's not possible to make amount 3 with coins 2 and 5. Since we can't combine the coin 2 and 5 to make the amount 3, the output is -1.
"""
"""
Constraints
- n = number of distinct denominations
- 1 <= n <= 100
- 1 <= coins[i],<= 10^3
- 0 <= amount <= 10^3
"""


class Solution:
    def f(self, ind, target, arr, dp):
        if target == 0:
            return 0

        if ind == 0:
            if arr[ind] != 0 and target % arr[ind] == 0:
                return target // arr[ind]

            return float("inf")

        if dp[ind][target] != -1:
            return dp[ind][target]

        notTake = 0 + self.f(ind - 1, target, arr, dp)
        take = float("inf")
        if arr[ind] != 0 and arr[ind] <= target:
            take = 1 + self.f(ind, target - arr[ind], arr, dp)

        dp[ind][target] = min(take, notTake)

        return min(take, notTake)

    def MinimumCoins(self, coins, amount):
        n = len(coins)
        if n < 2:
            return (
                amount // coins[0]
                if coins[0] != 0 and coins[0] <= amount and amount % coins[0] == 0
                else -1
            )

        dp = [[-1] * (amount + 1) for _ in range(n)]

        ans = self.f(n - 1, amount, coins, dp)

        return -1 if ans == float("inf") else ans


class SolutionOptimal:
    def MinimumCoins(self, coins, amount):
        n = len(coins)

        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for i in range(amount + 1):
            if coins[0] != 0 and i % coins[0] == 0:
                dp[0][i] = i // coins[0]

        for ind in range(1, n):
            for tar in range(1, amount + 1):
                notTake = 0 + dp[ind - 1][tar]
                take = float("inf")
                if coins[ind] != 0 and coins[ind] <= tar:
                    take = 1 + dp[ind][tar - coins[ind]]

                dp[ind][tar] = min(take, notTake)

        return dp[n - 1][amount] if dp[n - 1][amount] != float('inf') else -1


class SolutionOptimalSpace2D:
    def MinimumCoins(self, coins, amount):
        n = len(coins)

        prev, curr = [float('inf')] * (amount + 1), [float('inf')] * (amount + 1)

        # for i in range(n):
        prev[0] = 0

        for i in range(1, amount + 1):
            if coins[0] != 0 and i % coins[0] == 0:
                prev[i] = i // coins[0]

        for ind in range(1, n):
            curr = [float('inf')] * (amount + 1)
            curr[0] = 0
            for tar in range(1, amount + 1):
                notTake = 0 + prev[tar]
                take = float("inf")
                if coins[ind] != 0 and coins[ind] <= tar:
                    take = 1 + curr[tar - coins[ind]]

                curr[tar] = min(take, notTake)

            prev = curr

        return prev[amount] if prev[amount] != float('inf') else -1


s = SolutionOptimalSpace2D()

k1 = s.MinimumCoins([1, 2, 5], 11)

k2 = s.MinimumCoins([2, 5], 3)

print(k1)
print(k2)
