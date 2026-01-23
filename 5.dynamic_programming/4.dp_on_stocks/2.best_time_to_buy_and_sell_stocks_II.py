# Best time to buy and sell stocks II
"""
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock any number of times.

Holding at most one share of the stock at any given time is allowed,
meaning buying and selling the stock can be done any number of times,
but the stock must be sold before buying it again.
Buying and selling the stock on the same day is permitted.
"""
"""
Example 1:
Input: arr = [9, 2, 6, 4, 7, 3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4.
Then buy on day 4 (price = 4) and sell on day 5 (price = 7), profit = 7 - 4 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: arr = [2, 3, 4, 5, 6]
Output: 4
Explanation: Buy on day 1 (price = 2) and sell on day 5 (price = 6), profit = 6 - 2 = 4.
Total profit is 4.
"""
"""
Constraints
1 <= n<= 10^5
0 <= arr[i] <= 10^4
"""


class Solution:
    def f(self, ind, buy, arr, n, dp):
        if ind == n:
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]

        if buy:
            prof = max(
                -arr[ind] + self.f(ind + 1, 0, arr, n, dp),
                0 + self.f(ind + 1, 1, arr, n, dp),
            )
        else:
            prof = max(
                arr[ind] + self.f(ind + 1, 1, arr, n, dp),
                0 + self.f(ind + 1, 0, arr, n, dp),
            )

        dp[ind][buy] = prof
        return prof

    def stockBuySell(self, arr, n):
        dp = [[-1] * 2 for _ in range(n)]
        return self.f(0, 1, arr, n, dp)


class SolutionOptimal:
    def stockBuySell(self, arr, n):
        dp = [[0] * 2 for _ in range(n + 1)]

        dp[n][0], dp[n][1] = 0, 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    prof = max(
                        -arr[ind] + dp[ind + 1][0],
                        0 + dp[ind + 1][1],
                    )
                else:
                    prof = max(arr[ind] + dp[ind + 1][1], 0 + dp[ind + 1][0])

                dp[ind][buy] = prof

        return dp[0][1]


class SolutionOptimalSpace:
    def stockBuySell(self, arr, n):
        ahead = [0, 0]
        curr = [0, 0]

        ahead[0], ahead[1] = 0, 0

        for ind in range(n - 1, -1, -1):
            curr = [0, 0]
            for buy in range(2):
                if buy:
                    prof = max(
                        -arr[ind] + ahead[0],
                        0 + ahead[1],
                    )
                else:
                    prof = max(arr[ind] + ahead[1], 0 + ahead[0])

                curr[buy] = prof

            ahead = curr

        return ahead[1]



s = SolutionOptimalSpace()

k1 = s.stockBuySell([9, 2, 6, 4, 7, 3], 6)

k2 = s.stockBuySell([2, 3, 4, 5, 6], 5)

print(k1)
print(k2)
