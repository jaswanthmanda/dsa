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
    def stockBuySell(self, arr, n): ...
