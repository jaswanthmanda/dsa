# Best time to buy and sell stocks
"""
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock at most once.

The stock should be purchased before selling it, and both actions cannot occur on the same day.
"""
"""
Example 1:
Input: arr = [10, 7, 5, 8, 11, 9]
Output: 6
Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.


Example 2:
Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.
"""
"""
Constraints
1 <= n<= 105
0 <= arr[i] <= 106
"""


class Solution:
    def stockBuySell(self, arr, n):
        prof = 0
        minn = arr[0]
        for i in range(1, n):
            proff = arr[i] - minn
            prof = max(prof, proff)
            minn = min(minn, arr[i])

        return prof


s = Solution()

k1 = s.stockBuySell(
    [
        10,
        7,
        5,
        8,
        11,
        9,
    ],
    6,
)

k2 = s.stockBuySell(
    [
        5,
        4,
        3,
        2,
        1,
    ],
    5,
)

print(k1)
print(k2)
