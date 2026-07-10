# Best time to buy and sell stock

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104
"""

from typing import List


class Solution:
    def maxProfit(
        self,
        prices: List[int],
    ) -> int:
        # n
        n = len(prices)

        # base case
        if n == 1:
            return 0

        curr_max = prices[n - 1]
        max_ans = 0

        for i in range(n - 2, -1, -1):
            if prices[i] > curr_max:
                curr_max = prices[i]
            else:
                val = curr_max - prices[i]
                max_ans = max(max_ans, val)

        return max_ans
