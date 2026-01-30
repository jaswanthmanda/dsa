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
    def count(self, coins, N, amount): ...
