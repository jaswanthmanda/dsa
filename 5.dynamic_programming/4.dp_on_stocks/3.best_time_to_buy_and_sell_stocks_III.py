# Best time to buy and sell stocks III
"""
Given an array, arr, of n integers, where arr[i] represents the price of the stock on an ith day,
determine the maximum profit achievable by completing at most two transactions in total.

Holding at most one share of the stock at any time is allowed, meaning buying and selling the stock twice is permitted,
but the stock must be sold before buying it again.
Buying and selling the stock on the same day is allowed.
"""
"""
Example 1:
Input: arr = [4, 2, 7, 1, 11, 5]
Output: 15
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 7), profit = 7 - 2 = 5.
Then buy on day 4 (price = 1) and sell on day 5 (price = 11),
profit = 11 - 1 = 10.
Total profit is 5 + 10 = 15.


Example 2:
Input: arr = [1, 3, 2, 8, 4, 9]
Output: 12
Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 8), profit = 8 - 1 = 7.
Then buy on day 5 (price = 4) and sell on day 6 (price = 9),
profit = 9 - 4 = 5. Total profit is 7 + 5 = 12.
"""
"""
Constraints
- 1 <= n<= 105
- 0 <= arr[i] <= 106
"""


class Solution:
    def f(self, ind, buy, cap, arr, n):
        if cap == 0:
            return 0
        if ind == n:
            return 0

        if buy:
            prof = max(
                -arr[ind] + self.f(ind + 1, 0, cap, arr, n),
                0 + self.f(ind + 1, 1, cap, arr, n),
            )
        else:
            prof = max(
                arr[ind] + self.f(ind + 1, 1, cap - 1, arr, n),
                0 + self.f(ind + 1, 0, cap, arr, n),
            )

        return prof

    def stockBuySell(self, arr, n):
        return self.f(0, 1, 2, arr, n)


class SolutionOptimal:
    def f(self, ind, buy, cap, arr, n, dp):
        if cap == 0:
            return 0
        if ind == n:
            return 0

        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]

        if buy:
            prof = max(
                -arr[ind] + self.f(ind + 1, 0, cap, arr, n, dp),
                0 + self.f(ind + 1, 1, cap, arr, n, dp),
            )
        else:
            prof = max(
                arr[ind] + self.f(ind + 1, 1, cap - 1, arr, n, dp),
                0 + self.f(ind + 1, 0, cap, arr, n, dp),
            )

        dp[ind][buy][cap] = prof

        return prof

    def stockBuySell(self, arr, n):
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        return self.f(0, 1, 2, arr, n, dp)


class SolutionOptimalSpace:
    def stockBuySell(self, arr, n):
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for cap in range(1, 3):
                for buy in range(2):
                    if buy:
                        prof = max(
                            -arr[ind] + dp[ind + 1][0][cap],
                            0 + dp[ind + 1][1][cap]
                        )
                    else:
                        if cap - 1 >= 0:
                            prof = max(
                                arr[ind] + dp[ind + 1][1][cap - 1],
                                0 + dp[ind + 1][0][cap]
                            )

                    dp[ind][buy][cap] = prof

        return dp[0][1][2]


class SolutionOptimalSpaceMostOptimal:
    def stockBuySell(self, arr, n):
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for cap in range(1, 3):
                for buy in range(2):
                    if buy:
                        prof = max(
                            -arr[ind] + dp[ind + 1][0][cap],
                            0 + dp[ind + 1][1][cap]
                        )
                    else:
                        if cap - 1 >= 0:
                            prof = max(
                                arr[ind] + dp[ind + 1][1][cap - 1],
                                0 + dp[ind + 1][0][cap]
                            )

                    dp[ind][buy][cap] = prof

        return dp[0][1][2]


class SolutionOptimalSpaceMostOptimalPrevCurrent:
    def stockBuySell(self, arr, n):
        prev = [[0] * 3 for _ in range(2)]
        curr = [[0] * 3 for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            curr = [[0] * 3 for _ in range(2)]
            for cap in range(1, 3):
                for buy in range(2):
                    if buy:
                        prof = max(
                            -arr[ind] + prev[0][cap],
                            0 + prev[1][cap]
                        )
                    else:
                        if cap - 1 >= 0:
                            prof = max(
                                arr[ind] + prev[1][cap - 1],
                                0 + prev[0][cap]
                            )

                    curr[buy][cap] = prof

            prev = curr

        return prev[1][2]


s = SolutionOptimalSpaceMostOptimalPrevCurrent()

k1 = s.stockBuySell(
    [4, 2, 7, 1, 11, 5],
    6,
)

k2 = s.stockBuySell(
    [1, 3, 2, 8, 4, 9],
    6,
)

print(k1)
print(k2)
