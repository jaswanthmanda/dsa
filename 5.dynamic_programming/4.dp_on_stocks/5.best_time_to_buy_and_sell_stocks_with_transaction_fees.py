# Best time to buy and sell stocks with transaction fees
"""
Given an array arr where arr[i] represents the price of a given stock on the ith day. Additionally,
you are given an integer fee representing a transaction fee for each trade.
The task is to determine the maximum profit you can achieve such that you need to pay a transaction fee for each buy and sell transaction.
The Transaction Fee is applied when you sell a stock.

You may complete as many transactions.
You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before buying again).
"""
"""
Example 1:
Input: arr = [1, 3, 4, 0, 2], fee = 1
Output: 3
Explanation: Buy at day 1, sell at day 3, then, buy at day 4, sell at day 5.
Profit calculation: ((4 - 1) - 1) + ((2 - 0) - 1) = 2 + 1 = 3.

Example 2:
Input: arr = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: Buy at day 1 (price = 1), sell at day 4 (price = 8), then Buy at day 5 (price = 4), sell at day 6 (price = 9),
Profit calculation: ((9 - 4) - 2) + ((8 - 1) - 2)= 8.
"""
"""
Constraints
- 1 <= n<= 105
- 0 <= arr[i] ,fee<= 104
"""


class Solution:
    def stockBuySell(self, arr, n, fee):
        prev = [0] * (3)
        curr = [0] * (3)

        for ind in range(n - 1, -1, -1):
            curr = [0] * (3)
            for buy in range(2):
                if buy:
                    prof = max(
                        -arr[ind] + prev[0],
                        0 + prev[1],
                    )
                else:
                    prof = max(
                        (arr[ind] + prev[1]) - fee,
                        0 + prev[0],
                    )

                curr[buy] = prof

            prev = curr

        return prev[1]


s = Solution()

k1 = s.stockBuySell([1, 3, 4, 0, 2], 5, 1)

k2 = s.stockBuySell([1, 3, 2, 8, 4, 9], 6, 2)

print(k1)
print(k2)
