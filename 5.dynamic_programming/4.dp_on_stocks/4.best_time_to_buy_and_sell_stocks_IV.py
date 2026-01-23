# Best time to buy and sell stocks IV
"""
Given an array, arr, of n integers, where arr[i]
represents the price of the stock on an ith day,
determine the maximum profit achievable by completing at most k transactions in total.
Holding at most one share of the stock at any given time is allowed,
meaning buying and selling the stock k times is permitted,
but the stock must be sold before buying it again.
Buying and selling the stock on the same day is allowed.
"""
"""
Example 1:
Input: arr = [3, 2, 6, 5, 0, 3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3.
Total profit is 4 + 3 = 7.


Example 2:
Input: arr = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], k = 3
Output: 15
Explanation: Buy on day 1 (price = 1) and sell on day 3 (price = 4), profit = 4 - 1 = 3.
Then buy on day 4 (price = 2) and sell on day 6 (price = 7), profit = 7 - 2 = 5.
Then buy on day 7 (price = 2) and sell on day 9 (price = 9),
profit = 9 - 2 = 7. Total profit is 3 + 5 + 7 = 15.
"""
"""
Constraints
- 1 <= n<= 103
- 0 <= arr[i] <= 104
- 0 <= k <= 100
"""


class Solution:
    def stockBuySell(self, arr, n, k):
        # dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]
        prev = [[0] * (k + 1) for _ in range(2)]
        curr = [[0] * (k + 1) for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            curr = [[0] * (k + 1) for _ in range(2)]
            for cap in range(1, k + 1):
                for buy in range(2):
                    if buy:
                        prof = max(
                            -arr[ind] + prev[0][cap],
                            0 + prev[1][cap],
                        )
                    else:
                        if cap - 1 >= 0:
                            prof = max(
                                arr[ind] + prev[1][cap - 1],
                                0 + prev[0][cap],
                            )

                    curr[buy][cap] = prof
            prev = curr

        return prev[1][k]


s = Solution()

k1 = s.stockBuySell(
    [3, 2, 6, 5, 0, 3],
    6,
    2,
)

k2 = s.stockBuySell(
    [1, 2, 4, 2, 5, 7, 2, 4, 9, 0],
    10,
    3,
)

print(k1)
print(k2)
